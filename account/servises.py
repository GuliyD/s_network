from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


def base_form_servise(
        request,
        form_class,
        template_path_to_render: str,
        redirect_to: str,
        is_login=False,
        name_of_username_pole_to_register=None,
        name_of_password_pole_to_register=None,
        is_registration=False
):
    """returns function render or redirect"""
    is_redirect = False
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            if is_registration:
                user = form.save()
                login(request, user)
            elif is_login:
                username = form.cleaned_data(name_of_username_pole_to_register)
                password = form.cleaned_data(name_of_password_pole_to_register)
                user = authenticate(request, username, password)
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
