# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from blogs.views import UpdateUserDataView
from loginsystem import views
from loginsystem.views import ProfileView


admin.autodiscover()


urlpatterns = patterns('',
                       # (r'^logout/', LogoutView.as_view()),
                       (r'^logout/', views.LogoutView.as_view()),
                       (r'^login/',  views.LoginView.as_view()),
                       (r'^sign-up/', views.SignupView.as_view()),
                       url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
                       url(r'^profile/edit/$', UpdateUserDataView.as_view(), name="user-edit"),
                       # url(r'^profile/commit/$', CommitListView.as_view(), name="user-commit"),
                       # создай страницу профиля с информацию о себе, список последних коммитов, с возможностью посмотреть их на отдельной странице, а также последними постами в блоге

)