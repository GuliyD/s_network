from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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
