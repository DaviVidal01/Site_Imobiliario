from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Imoveis(models.Model):
    OPTIONS_TYPE = [
        ("APARTMENT","Apartment"),
        ("VILLA HOUSE","Villa House"),
        ("PENTHOUSE","Penthouse"),
    ]

    OPTIONS_STATUS = [
        ("DISPONÍVEL","Disponível"),
        ("VENDIDO","Vendido"),
    ]

    address = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=100, choices=OPTIONS_STATUS, default='')
    area = models.IntegerField(max_length=4, default=0)
    bedrooms = models.IntegerField(max_length=4, default=0)
    bathrooms = models.IntegerField(max_length=4, default=0)
    floor = models.IntegerField(max_length=4, default=0)
    parking = models.IntegerField(max_length=4, default=0)
    value = models.DecimalField(max_digits=5,decimal_places=2)
    tipo = models.CharField(max_length=100, choices=OPTIONS_TYPE, default='')
    path = models.ImageField(upload_to="images/", blank=True)



class Message(models.Model):

    name = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    email = models.CharField(max_length=50, default='', null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=255, default='', null=False, blank=False)
