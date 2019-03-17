from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from views import index, page, upload
from blogs.views import AboutView, PostListView
# from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', index),
                       url(r'^blog/(?P<blog_id>\d+)/$', page),
                       url(r'^upload/', upload),
                       (r'^about/', AboutView.as_view()),
                       (r'post_list/', PostListView.as_view())
# (r'^about/', AboutView.as_view()),

    # Examples:
    # url(r'^$', 'news.views.home', name='home'),
    # url(r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)