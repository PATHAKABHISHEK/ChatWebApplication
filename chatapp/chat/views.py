from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return render(request=request,template_name='chat/register.html',
                    context={'title':'Register Here'})

def login(request):
    return render(request=request,template_name='chat/login.html',
                    context={'title':'Login Here'})
