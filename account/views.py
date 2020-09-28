from django.shortcuts import render
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .services import (
    add_profile_photo_service,
    change_profile_photo_service,
    add_work_service,
    get_all_current_user_works,
    home_page_service,
    comment_view_service,
    like_view_service
)


def home(request):
    response = home_page_service(request)
    return response


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
