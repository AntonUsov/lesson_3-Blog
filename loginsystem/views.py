# -*- coding: utf-8 -*-
from decimal import Context

from django.contrib import auth
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

from blogs.models import Post, User, Commit
from blogs.views import BaseView


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


class LoginView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)


class SignupView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/auth/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "sign-up.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(SignupView, self).form_valid(form)


class ProfileView(BaseView, TemplateView, LoginView):
    # model = Post, User
    template_name = 'profile.html'
    # context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        commit_list = Commit.objects.all().filter(user=self.blog_user)
        # context['user_data'] = User.objects.filter(user=self.blog_user)
        context['news_list'] = Post.objects.filter(user=self.blog_user)
        context['commit_list'] = commit_list.order_by('-timestamp')[:5]
        return context


# def login(request):
#     args = {}
#     args.update(csrf(request))
#     if request.POST:
#         username = request.POST.get['username', '']
#         password = request.POST.get['password', '']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 auth.login(request, user)
#                 return redirect('/')
#             else:
#                 args['login_error'] = "Пользователь не найден"
#                 return render_to_response('/login.html', args)
#         else:
#             return render_to_response('/login.html', args)


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
#
#
# class LogoutView(TemplateView):
#     template_name = 'loginsystem/logout.html'
#     context_object_name = 'logout'


# class SignupView(TemplateView):
#     template_name = 'loginsystem/sign-up.html'
#     context_object_name = 'Sign-up'


# class LoginView(TemplateView):
#     template_name = 'loginsystem/login.html'
#     context_object_name = 'login'





