from django.urls import path
from . import views

urlpatterns = [
    # ------ Guest Pages
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('details/<int:id>', views.properties_details, name='properties_details'),
    # ------ Admin Pages
]