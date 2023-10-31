from django.urls import path
from . import views

urlpatterns = [
    # ------ Guest Pages
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('details/<int:id>', views.properties_details, name='properties_details'),
    # ------ Admin Pages
    path('funcionario/', views.funcionario, name="funcionario"),
    # ------ CRUD
    path('publish/',views.publish_message, name="publish_message"),
]