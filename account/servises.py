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
    for i in works:
        print(i.photo.url)
    return render(request, 'account/home.html', {'works': works})