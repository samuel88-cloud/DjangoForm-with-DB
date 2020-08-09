from django.db import models
from phone_field import PhoneField


# Create your models here.
class ClientDetails(models.Model):
    full_name=models.CharField(max_length=20)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    client_value=models.FloatField(help_text='Enter in USD')
    email=models.EmailField()
    website= models.CharField(max_length = 200)    

    def __str__(self):
        return self.full_name
