from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def base_form_servise(
        request,
        form_class,
        template_path_to_render: str,
        redirect_to: str,

        is_login=False,

        is_registration=False,

        is_update_current_user=False,
):
    """returns render or redirect, can't update model,
    can register user, login, create new pole in ModelForm"""
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
            elif is_update_current_user:
                username_to_update = form.cleaned_data.get('username')
                password_to_update = form.cleaned_data.get('password')
                email_to_update = form.cleaned_data.get('email')
                profile_photo_to_update = form.cleaned_data.get('profile_photo')
                update_current_user(
                    request,
                    username=username_to_update,
                    password=password_to_update,
                    email=email_to_update,
                    profile_photo=profile_photo_to_update
                )
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


def update_current_user(request, username=None, password=None, email=None, profile_photo=None):
    if username:
        request.user.update(username=username)
    if password:
        request.user.set_password(password)
    if email:
        request.user.update(email=email)
    if profile_photo:
        request.user.update(profile_photo=profile_photo)

    return 'done'
