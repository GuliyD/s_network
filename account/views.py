from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, logout, login
from user.forms import RegistrationForm
from .forms import UserPhotoForm, LoginForm, CommentForm
from .models import UserWorkModel, CommentModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .servises import (
    base_form_service,
    add_profile_photo_service,
    change_profile_photo_service,
    add_work_service,
    get_all_current_user_works,
    home_page_service
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
    try:
        work = UserWorkModel.objects.get(id=work_id)
    except UserWorkModel.DoesNotExist:
        return redirect('account:home')
    if not request.user in [com for com in work.liked.all()]:
        work.liked.add(request.user)
        work.like_value = 'Unlike'
        work.save()
    else:
        work.liked.remove(request.user)
        work.like_value = 'Like'
        work.save()
    return redirect('home')


@login_required
def comment_view(request, work_id):
    try:
        work = request.user.works.get(id=work_id)
        comments = work.comments.all()
    except CommentModel.DoesNotExist:
        comments = []
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            work.comments.create(comment=comment, user=request.user)
            return render(request, 'account/comment.html', {'form': CommentForm(), 'comments': comments})
    else:
        form = CommentForm()
    return render(request, 'account/comment.html', {'form': form, 'comments': comments})