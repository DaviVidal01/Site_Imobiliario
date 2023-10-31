from django.shortcuts import render
from .models import Message, Imoveis
from .forms import LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# -------- Guest Page
def index(request):
    imoveis_view = Imoveis.objects.all()
    message_view = Message.objects.all()
    return render(request, 'index.html', {'imoveis': imoveis_view, 'message': message_view})

def properties(request):
    imoveis_view = Imoveis.objects.all()
    return render(request, 'properties.html', {'imoveis': imoveis_view})

def properties_details(request):
    imoveis_view = Imoveis.objects.all()
    return render(request, 'properties-details.html', {'imoveis': imoveis_view})

def contact(request):
    message_view = Message.objects.all()
    return render(request, 'contact.html', {'message': message_view})

# -------- Admin Page

# -------- Login View



# -------- CRUD View