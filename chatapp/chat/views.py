from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from .models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.user_name = form.cleaned_data['user_name']
            user.email_id = form.cleaned_data['email_id']
            user.password = form.cleaned_data['password']
            user.save()
            login(request, user)
            return redirect(request, '/')

    else:
        form = RegistrationForm()
        return render(request=request,template_name='chat/register.html',
                    context={'title':'Register Here', 'form':form})

def login_page(request):
    return render(request=request,template_name='chat/login.html',
                    context={'title':'Login Here'})


def dashboard(request):
    return render(request=request,template_name='chat/dashboard.html',
                    context={'title':'Chat Here'})

def logout_page(request):
    logout(request)
    return redirect(request, '/')
