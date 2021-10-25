from django.db import models
from django_countries.fields import CountryField


class AddressBook(models.Model):
    """Address Book model"""
    name = models.CharField(null=False, max_length=50)
    street = models.CharField(null=False, max_length=100)
    street2 = models.CharField(max_length=100)
    zip = models.CharField(null=False, max_length=10)
    # Longest city name is 85 Characters
    city = models.CharField(max_length=85)
    state = models.CharField(max_length=100)
    # Label for form view
    country = CountryField(null=False, blank_label="(Select Country)")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    owner = models.ForeignKey(
        'auth.User', related_name='addressbook', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "country", "street", "zip", "owner")
