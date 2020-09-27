from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import ProfileModel, UserWorkModel
from .forms import UserPhotoForm
from user.models import User


def base_form_service(
        request,
        form_class,
        template_path_to_render: str,
        redirect_to: str,

        is_login=False,

        is_registration=False,
):
    """returns render or redirect, can't update model,
    can register user, login, create new poles in ModelForm"""
    is_redirect = False
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            if is_registration:
                user = form.save()
                login(request, user)
            elif is_login:
                username = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                login(request, user)
            else:
                form.save()
            redirect_return = redirect(redirect_to)
            is_redirect = True
    else:
        form = form_class()
    render_return = render(request, template_path_to_render, {'form': form})
    if is_redirect:
        response = redirect_return
    else:
        response = render_return
    return response


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
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            img = request.FILES['photo']
            UserWorkModel.objects.create(
                user=user,
                photo=img
            )
            return redirect('account:account')
    else:
        form = UserPhotoForm()
    return render(request, 'account/change_profile_photo.html', {'form': form})


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
    if not(request.user in [com for com in work.liked.all()]):
        print('like')
        work.liked.add(request.user)
        work.save()
    else:
        work.liked.remove(request.user)
        work.save()
    works = UserWorkModel.objects.all()
    works_and_likes = get_works_and_likes(request, works)
    return render(request, 'account/home.html', {'works_and_likes': works_and_likes})