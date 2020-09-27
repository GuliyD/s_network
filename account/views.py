from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, logout, login
from user.forms import RegistrationForm
from .forms import UserPhotoForm, LoginForm, CommentForm
from .models import UserWorkModel, CommentModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .services import (
    base_form_service,
    add_profile_photo_service,
    change_profile_photo_service,
    add_work_service,
    get_all_current_user_works,
    home_page_service,
    comment_view_service,
    like_view_service
)


def create_user_view(request):
    response = base_form_service(request,
                                 form_class=RegistrationForm,
                                 template_path_to_render='account/register.html',
                                 redirect_to='home',
                                 is_registration=True
                                 )
    return response


def home(request):
    response = home_page_service(request)
    return response


def logout_view(request):
    logout(request)
    return HttpResponse('logautnuto')


@login_required
def account_view(request):
    works = get_all_current_user_works(request)
    return render(request, 'account/account.html', {'works': works})


@login_required
def change_profile_photo_view(request):
    response = change_profile_photo_service(request)
    return response


@login_required
def add_profile_photo_view(request):
    response = add_profile_photo_service(request)
    return response


def login_view(request):
    response = base_form_service(
                                 request,

                                 is_login=True,

                                 form_class=LoginForm,
                                 template_path_to_render='account/login.html',
                                 redirect_to='home'
                                 )
    return response


@login_required
def add_work_view(request):
    response = add_work_service(request)
    return response


@login_required
def like_view(request, work_id):
    response = like_view_service(request, work_id)
    return response

@login_required
def comment_view(request, work_id):
    response = comment_view_service(request, work_id, CommentForm)
    return response
