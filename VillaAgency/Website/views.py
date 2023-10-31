from django.shortcuts import render
from .models import Message, Imoveis
from .forms import LoginForms, MessageForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# -------- Guest Page
def index(request):
    login_form = LoginForms()
    message_form = MessageForms()
    imoveis_view = Imoveis.objects.all()
    return render(request, 'index.html', {'imoveis': imoveis_view, 'message': message_form, 'user':login_form})

def properties(request):
    login_form = LoginForms()
    imoveis_view = Imoveis.objects.all()
    return render(request, 'properties.html', {'imoveis': imoveis_view, 'user':login_form})

def properties_details(request,id):
    login_form = LoginForms()
    imoveis_view = Imoveis.objects.get(pk=id)
    return render(request, 'properties-details.html', {'imoveis': imoveis_view, 'user':login_form})

def contact(request):
    login_form = LoginForms()
    message_form = MessageForms()
    return render(request, 'contact.html', {'message': message_form, 'user':login_form})

# -------- Admin Page

# -------- Login View
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

    if form.is_valid():
        email = form['email_form'].value()
        password = form['senha_form'].value()
        user_temp = User.objects.get(email= email)

        usuario = auth.authenticate(
            request,
            email = user_temp,
            password = password
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request, 'Login efetuado com sucesso!')
            if usuario.username == "admin":
                return redirect('funcionario')
            return redirect('index')
    else:
        messages.error(request, f' Erro ao realizar o login!')
        return redirect('index')
    
    return render(request, 'index.html', {'user': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

# -------- CRUD View

def publish_message(request):
    forms = MessageForms
    if request.method == "POST":
        forms = MessageForms(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'imagem cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "index.html",{"message":forms})