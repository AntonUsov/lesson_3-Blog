# -*- coding: utf-8 -*-
import datetime

from django.core.urlresolvers import reverse
from django.template import loader, Context

from models import Post, User, Commit
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.context_processors import csrf
from django.contrib import auth
from django.forms import ModelForm


class BaseView(object):
    user = None
    blog_user = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous():
            self.user = request.user
            try:
                self.blog_user = User.objects.get(user=self.user)
            except:
                self.blog_user = None
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['context_user'] = self.user
        context['blog_user'] = self.blog_user
        context['request'] = self.request
        return context


# class AboutView(TemplateView):
#     template_name = 'blogs/about.html'
#
#     def get_queryset(self):
#         return Post.objects.all()

class PostListView(BaseView, ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'blogs/post_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date')

    # def get(self, request, *args, **kwargs):
    #
    #     self.object_list = self.get_queryset()
    #     allow_empty = self.get_allow_empty()
    #     if not allow_empty and len(self.object_list) == 0:
    #         raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
    #                       % {'class_name': self.__class__.__name__})
    #     #context = self.get_context_data(object_list=self.object_list.filter())
    #     news_list = Post.objects.all().order_by('-pub_date')
    #     user_list = User.objects.all()
    #     context = Context({
    #         'news_list_param': self.get_context_data(object_list=self.object_list.filter()),
    #         'username': request.user.username
    #         #'user_list': user_list,
    #         # 'username': auth.get_user(request).username,
    #     })
    #     return self.render_to_response(context)

    def get_paginate_by(self, queryset):
        """
        Get the number of items to paginate by, or ``None`` for no pagination.
        """
        return self.paginate_by

    # def head(self):
    #     last_post = self.get_queryset().latest('pub_date')
    #     response = HttpResponse('')
    #     response['Last-Modified'] = last_post.pub_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    #     return response


class MAinPagesView(BaseView, TemplateView):
    template_name = 'blogs/index.html'
    # model = Post
    # context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(MAinPagesView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all().order_by('-pub_date'),
        context['user_list'] = User.objects.all(),
        return context

    def get_context_data(self, *args, **kwargs):
        context_list = super(MAinPagesView, self).get_context_data(*args, **kwargs)
        # context = super(AboutUs, self).get_context_data(*args, **kwargs)
        post_list = Post.objects.all().order_by('-pub_date')
        user_list = User.objects.all()
        context_list = ({
            'post_list': post_list,
            'user_list': user_list,

        })
        return context_list


def index(request):
    news_list = Post.objects.all().order_by('-pub_date')[:20]
    # text = Post.text
    user_list = User.objects.all()
    template = loader.get_template('blogs/index.html')
    context = Context({
        'news_list_param': news_list,
        # 'text': text,
        'user_list': user_list,
        'username': auth.get_user(request).username,
    })
    return HttpResponse(template.render(context))


def upload(request):
    post = u'привет мир'
    template = loader.get_template('blogs/upload.html')
    context = Context({
        'post': post,

    })
    return HttpResponse(template.render(context))


class PageView(BaseView, DetailView):
    template_name = 'blogs/post.html'
    model = Post

    def get_queryset(self):
        #  чтобы ограничить выборку
        return Post.objects.all()


class CommitDetailView(BaseView, DetailView):
    template_name = 'blogs/commit.html'
    model = Commit

    def get_queryset(self):
        #  чтобы ограничить выборку
        return Commit.objects.all()

class BlogUpdateForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']


class UpdateBlogView(BaseView, UpdateView):
    template_name = 'blogs/post_update.html'
    form_class = BlogUpdateForm
    success_url = '/'

    def get_queryset(self):
        return Post.objects.filter(user=self.blog_user)


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['status', 'bio', 'date_of_birth']
        # exclude = ['user']


class UpdateUserDataView(BaseView, UpdateView):
    template_name = 'blogs/user_update.html'
    form_class = UserUpdateForm
    # success_url = reverse('profile')

    def get_object(self, queryset=None):
        return self.blog_user

    def get_success_url(self):
        return reverse('profile') + '?good'
    # def get_queryset(self):
    #     return User.objects.filter(user=self.blog_user)


class CreateBlogView(BaseView, CreateView):
    template_name = 'blogs/post_update.html'
    form_class = BlogUpdateForm

    def get_success_url(self):
        return reverse('profile')

    def get_queryset(self):
        return Post.objects.filter(user=self.blog_user)

    def form_valid(self, form):
        form.instance.pub_date = datetime.datetime.now()
        form.instance.user = self.blog_user
        return super(CreateBlogView, self).form_valid(form)


class DeleteBlogView(BaseView, DeleteView):
    template_name = 'blogs/post_delete.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.blog_user)

    def get_success_url(self):
        return reverse('home')


# class CommitListView(BaseView, ListView):
#     template_name = 'user-commit'
#     model = Commit
#     context_object_name = 'commit'
#
#     def get_queryset(self):
#         return Commit.objects.all().order_by('-pub_date')[:5]
