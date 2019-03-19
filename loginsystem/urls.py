from django.conf.urls import patterns, include, url
from django.contrib import admin
from loginsystem.views import LogoutView, LoginView, SignupView
admin.autodiscover()


urlpatterns = patterns('',
                       # (r'^logout/', LogoutView.as_view()),
                       (r'^logout/', LogoutView.as_view()),
                       (r'^login/', LoginView.as_view()),
                       (r'^sign-up/', SignupView.as_view()),

)