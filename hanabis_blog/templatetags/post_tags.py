from allauth.socialaccount.models import SocialAccount
from django import template
from django.contrib.auth.models import User

from hanabis_blog.models import Tag, Post


register = template.Library()

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.inclusion_tag('hanabis_blog/tags/last_posts.html')
def get_last_posts(count=4):
    posts = Post.objects.order_by('id')[:count]
    # print(posts)
    return {"last_posts":posts}

#
@register.inclusion_tag('hanabis_blog/tags/popular_posts.html')
def get_popular_posts(count=5):
    posts = Post.objects.order_by('id')[:count]
    # print(posts)
    return {"popular_posts":posts}

#
# @register.inclusion_tag('hanabis_blog/tags/post_list.html')
# def get_all_posts():
#     post_list = Post.objects.all()
#     # print(posts)
#     return {"post_list":post_list}

