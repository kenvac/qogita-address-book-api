
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressBookSerializer
from .models import AddressBook


class AddressBookViews(APIView):
    """Address Book api methods"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results,
        or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(
            queryset,
            self.request,
            view=self
        )

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object
        for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def _get_address_object(self, request, id):
        """Get address object from id with filter on requested user"""
        return get_object_or_404(AddressBook, id=id, owner=request.user.id)

    def post(self, request):
        request.data["owner"] = request.user.id
        serializer = AddressBookSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, format=None):
        query_params = request.query_params
        many = True
        if id:
            items = self._get_address_object(request, id)
            many = False
        elif query_params and 'zip' in query_params:
            zip = query_params.get("zip")
            items = get_list_or_404(
                AddressBook, zip=zip, owner=request.user.id)
        else:
            items = get_list_or_404(AddressBook, owner=request.user.id)
        if many:
            page = self.paginate_queryset(items)
            if page is not None:
                serializer = AddressBookSerializer(page, many=many)
                return self.get_paginated_response(serializer.data)

        serializer = AddressBookSerializer(items, many=many)
        return Response({"status": "success", "data": serializer.data},
                        status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = self._get_address_object(request, id)
        serializer = AddressBookSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(AddressBook, id=id, owner=request.user.id)
        item.delete()
        return Response({"status": "success", "data": "Address Deleted"})


class AddressBookBatchDelete(APIView):
    """Address Book api methods"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Batch address delete post method. We are keeping this code separate
        to have more control of batch control method over delete method
        """

        data = request.data
        if "ids" in data:
            ids = data.get("ids")
            if not isinstance(data.get("ids"), list):
                return Response({"status": "error",
                                 "reason": "ids param must of list type",
                                 "data": data},
                                status=status.HTTP_400_BAD_REQUEST)

            # Record id not found are ignored
            items = AddressBook.objects.filter(
                id__in=ids, owner=request.user.id)
            if not items.count() > 0:
                return Response({"status": "error",
                                 "reason": "No addresses found",
                                 "data": data},
                                status=status.HTTP_400_BAD_REQUEST)

            items.delete()
            return Response({"status": "success",
                             "reason": "Addresses Deleted",
                             "data": data})

        return Response({"status": "error",
                         "reason": "ids param not found",
                         "data": data},
                        status=status.HTTP_400_BAD_REQUEST)
