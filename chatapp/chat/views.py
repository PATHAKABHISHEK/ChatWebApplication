from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            messages.success(request, f'Successufully Logged as {username}')
            login(request, user)
            return redirect("chat:dashboard")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = RegistrationForm()
    return render(request=request,template_name='chat/register.html',
                context={'title':'Register Here', 'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully")
    return redirect('chat:homepage')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, f'Successufully Logged as {username}')
                login(request, user)
                return redirect('chat:dashboard')
            else:
                messages.error(request, 'Something went wrong')
        else:
            messages.error(request,'Something Went Wrong')

    form = AuthenticationForm()
    return render(request=request,template_name='chat/login.html',
                context={'title':'Login Here', 'form': form})


def dashboard(request):
    return render(request=request,template_name='chat/dashboard.html',
                    context={'title':'Chat Here'})
