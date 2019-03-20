from django.conf.urls import patterns, include, url
from django.contrib import admin

from loginsystem import views



admin.autodiscover()


urlpatterns = patterns('',
                       # (r'^logout/', LogoutView.as_view()),
                       (r'^logout/', views.LogoutView.as_view()),
                       (r'^login/',  views.LoginView.as_view()),
                       (r'^sign-up/', views.SignupView.as_view()),
                       создай страницу профиля с информацию о себе, список последних коммитов, с возможностью посмотреть их на отдельной странице, а также последними постами в блоге

)