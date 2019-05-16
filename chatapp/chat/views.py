from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register_login(request):
    return render(request=request,template_name='chat/register_login.html',
                    context={'title':'ChatApp'})
