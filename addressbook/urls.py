from django.conf.urls import url
from django.urls import path
from .views import AddressBookBatchDelete, AddressBookViews

urlpatterns = [
    path('addressbook', AddressBookViews.as_view(), name='addressbook-list'),
    path('addressbook/<int:id>', AddressBookViews.as_view(),
         name='addressbook-detail'),
    path('addressbook/batchdelete', AddressBookBatchDelete.as_view(),
         name='addressbook-batch-delete'),
    url(r'addressbook/(?P<pk>[0-9]+)$',
        AddressBookViews, name='addressbook-params-search'),
]
