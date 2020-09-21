from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from user.forms import RegistrationForm
from .forms import UserPhotoForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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


@login_required
def account_view(request):
    response = base_form_servise(
                                 request,
                                 form_class=UserPhotoForm,
                                 template_path_to_render='account/account.html',
                                 redirect_to='home',
                                 is_update_current_user=True,
                                 )
    return response



def login_view(request):
    response = base_form_servise(
                                 request,

                                 is_login=True,

                                 form_class=LoginForm,
                                 template_path_to_render='account/login.html',
                                 redirect_to='home'
                                 )
    return response