from django import template
from hanabis_blog.models import Tag, Post


register = template.Library()

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.inclusion_tag('hanabis_blog/tags/last_posts.html')
def get_last_posts(count=3):
    posts = Post.objects.order_by('id')[:count]
    # print(posts)
    return {"last_posts":posts}


@register.inclusion_tag('hanabis_blog/tags/popular_posts.html')
def get_popular_posts():
    posts = Post.objects.order_by('id')[:6]
    # print(posts)
    return {"last_posts":posts}


