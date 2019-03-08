from django.template import loader, Context

from models import Post, User
from django.http import HttpResponse


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


def page(request, blog_id):
    post = Post.objects.get(id=blog_id)
    template = loader.get_template('blogs/post.html')
    context = Context({
        'post': post,

    })
    return HttpResponse(template.render(context))
