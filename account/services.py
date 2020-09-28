from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import ProfileModel, UserWorkModel
from .forms import UserPhotoForm, WorkForm
from user.models import User





def add_profile_photo_service(request):
    try:
        if request.user.profile.photo:
            return redirect('account:change_profile_photo')
    except ProfileModel.DoesNotExist:
        pass

    if request.POST:
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            img = form.cleaned_data.get("photo")
            try:
                profile = request.user.profile
                profile.photo = img
            except ProfileModel.DoesNotExist:
                profile = ProfileModel.objects.create(
                    user=request.user,
                    photo=img
                )
            profile.save()
            return redirect('account:account')
    else:
        form = UserPhotoForm()
    return render(request, 'account/add_profile_photo.html', {'form': form})


def change_profile_photo_service(request):
    if request.POST:
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.photo.delete()
            profile.photo = request.FILES['photo']
            profile.save()
            return redirect('account:account')
    else:
        form = UserPhotoForm()
    return render(request, 'account/change_profile_photo.html', {'form': form})


def add_work_service(request):
    if request.POST:
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work_name = form.cleaned_data.get('work_name')
            user = request.user
            img = request.FILES['photo']
            UserWorkModel.objects.create(
                work_name=work_name,
                user=user,
                photo=img
            )
            return redirect('account:account')
    else:
        form = WorkForm()
    return render(request, 'account/add_work.html', {'form': form})


def get_all_current_user_works(request):
    return request.user.works.all()


def home_page_service(request):
    works = UserWorkModel.objects.all()
    works_and_likes = get_works_and_likes(request, works)
    return render(request, 'account/home.html', {'works_and_likes': works_and_likes})


def get_works_and_likes(request, works):
    users_in_works = [i.liked for i in works]
    print(users_in_works)
    likes_for_works = list(map(lambda users: 'Unlike' if request.user in users.all() else 'Like', users_in_works))
    works_and_likes = list(zip(works, likes_for_works))
    return works_and_likes


def comment_view_service(request, work_id, form_class):
    work = UserWorkModel.objects.get(id=work_id)
    try:
        comments = work.comments.all()
    except UserWorkModel.DoesNotExist:
        comments = []
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            work.comments.create(comment=comment, user=request.user)
            return render(request, 'account/comment.html', {'form': form_class(), 'comments': comments})
    else:
        form = form_class()
    return render(request, 'account/comment.html', {'form': form, 'comments': comments})


def like_view_service(request, work_id):
    try:
        work = UserWorkModel.objects.get(id=work_id)
    except UserWorkModel.DoesNotExist:
        return redirect('account:home')
    if not(request.user in [user_liked for user_liked in work.liked.all()]):
        print('like')
        work.liked.add(request.user)
        work.save()
    else:
        work.liked.remove(request.user)
        work.save()
    works = UserWorkModel.objects.all()
    works_and_likes = get_works_and_likes(request, works)
    return render(request, 'account/home.html', {'works_and_likes': works_and_likes})