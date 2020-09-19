from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from user.forms import RegistrationForm
from django.http import HttpResponse
from .servises import (
    base_form_servise
)


def create_user_view(request):
    response = base_form_servise(request,
                                 form_class=RegistrationForm,
                                 template_path_to_render='account/register.html',
                                 redirect_to='home',
                                 is_registration=True
                                 )
    return response


def home(request):
    return HttpResponse('rabotaet')


def logout_view(request):
    logout(request)
    return HttpResponse('logautnuto')
