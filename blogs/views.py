# -*- coding: utf-8 -*-
from django.template import loader, Context

from models import Post, User
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView


class AboutView(TemplateView):
    template_name = 'blogs/about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'blogs/post_list.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        # user_list = User.objects.all()
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list.filter())
        # context = self.object_list.filter( Post.user.name['User_A'] )
        return self.render_to_response(context)

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


def index(request):
    news_list = Post.objects.all().order_by('-pub_date')[:20]
    # text = Post.text
    user_list = User.objects.all()
    template = loader.get_template('blogs/index.html')
    context = Context({
        'news_list_param': news_list,
        # 'text': text,
        'user_list': user_list,
    })
    return HttpResponse(template.render(context))


def upload(request):
    post = u'привет мир'
    template = loader.get_template('blogs/upload.html')
    context = Context({
        'post': post,

    })
    return HttpResponse(template.render(context))


def page(request, blog_id):
    post = Post.objects.get(id=blog_id)
    template = loader.get_template('blogs/post.html')
    context = Context({
        'post': post,

    })
    return HttpResponse(template.render(context))
