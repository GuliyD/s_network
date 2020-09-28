from django.shortcuts import render
from .services import base_form_service
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout


def create_user_view(request):
    response = base_form_service(request,
                                 form_class=RegistrationForm,
                                 template_path_to_render='user/register.html',
                                 redirect_to='account:home',
                                 is_registration=True
                                 )
    return response


def logout_view(request):
    logout(request)
    return HttpResponse('logautnuto')


def login_view(request):
    response = base_form_service(
                                 request,

                                 is_login=True,

                                 form_class=LoginForm,
                                 template_path_to_render='user/login.html',
                                 redirect_to='account:home'
                                 )
    return response
