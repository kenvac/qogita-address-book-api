from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import AddressBook


class AddressBookSerializer(serializers.ModelSerializer):
    """Address Book object serializer"""

    street2 = serializers.CharField(required=False, max_length=100)
    city = serializers.CharField(required=False, max_length=85)
    state = serializers.CharField(required=False, max_length=100)
    country = CountryField(country_dict=True)
    phone_number = serializers.CharField(required=False, max_length=15)
    email = serializers.EmailField(required=False)

    class Meta:
        model = AddressBook
        fields = ("__all__")
