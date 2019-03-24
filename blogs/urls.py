from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, upload, PageView, UpdateBlogView, CreateBlogView, DeleteBlogView, MAinPagesView, \
    CommitDetailView

# from blogs.views import AboutView


admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/new/$', CreateBlogView.as_view(), name="blog-new"),
                       url(r'^blog/(?P<pk>\d+)/$', PageView.as_view(), name="blog-detail"),
                       url(r'^commit/(?P<pk>\d+)/$', CommitDetailView.as_view(), name="commit-detail"),
                       url(r'^blog/(?P<pk>\d+)/update/$', UpdateBlogView.as_view(), name="blog-update"),
                       url(r'^blog/(?P<pk>\d+)/delete/$', DeleteBlogView.as_view(), name="blog-delete"),
                       url(r'^upload/', upload),
                       # url(r'^about/', AboutView.as_view()),
                       # (r'post_list/', PostListView.as_view()),
                       url(r'^auth/', include('loginsystem.urls')),
                       url(r'^$',  MAinPagesView.as_view(), name="home"),


# (r'^about/', AboutView.as_view()),


)