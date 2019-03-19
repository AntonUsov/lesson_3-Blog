# -*- coding: utf-8 -*-
from django.contrib import auth
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get['username', '']
        password = request.POST.get['password', '']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('/login.html', args)
        else:
            return render_to_response('/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


class LogoutView(TemplateView):
    template_name = 'loginsystem/logout.html'
    context_object_name = 'logout'


class SignupView(TemplateView):
    template_name = 'loginsystem/sign-up.html'
    context_object_name = 'Sign-up'


class LoginView(TemplateView):
    template_name = 'loginsystem/login.html'
    context_object_name = 'login'





