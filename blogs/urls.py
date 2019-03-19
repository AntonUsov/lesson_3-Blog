from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, page, upload
from blogs.views import AboutView, PostListView


admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/(?P<blog_id>\d+)/$', page),
                       url(r'^upload/', upload),
                       (r'^about/', AboutView.as_view()),
                       (r'post_list/', PostListView.as_view()),
                       url(r'^auth/', include('loginsystem.urls')),
                       url(r'^$', index),
# (r'^about/', AboutView.as_view()),

    # Examples:
    # url(r'^$', 'news.views.home', name='home'),
    # url(r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)