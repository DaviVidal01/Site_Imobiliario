from django.contrib import admin
from .models import Imoveis, Message
# Register your models here.


admin.site.register(Imoveis),
admin.site.register(Message)