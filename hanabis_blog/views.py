import django
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Post, Tag, Author
from django.core.paginator import Paginator
# class PostsView(ListView):
#     model = Post
#     queryset = Post.objects.filter(draft=False)
# #

class TagYear:

    def get_tags(self):
        return Tag.objects.all()

    def get_year(self):
        Post.objects.filter(draft=True)



class PostsView(TagYear, ListView):
    paginate_by = 3
    post_list = Post
    queryset = Post.objects.filter(draft=False)




class TagView(ListView):
    tag_list = Tag
    queryset = Tag.objects.all()

    # def get(self, requests):
    #     tags = Tag.objects.all()
    #     return render(requests, 'tags/tags_list.html', {'tags_list':tags})
#

class PostDetailView(DetailView):
    model = Post
    slug_field = "slug"

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get('parent'))
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'hanabis_blog/author_detail.html'
    slug_field = "slug"

class TagDetailView(ListView):
    model = Tag
    slug_field = "slug"



class Search(ListView):

    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context





""" Filters. Need to make HTML templates"""

class FilterPostsView(TagYear, ListView):

    def get_queryset(self):
        queryset = Post.objects.filter(
            Q(date_pub__in=self.request.GET.getlist("date")) |
            Q(categories__in=self.request.GET.getlist("category"))
        )
        return queryset

    # def get_context_data(self, *args, **kwargs):
    #     context = super.get_context_data(*args, **kwargs):
    #     context['date_pub'] = ''.join([f"date_pub={x}&" for x in self.request.GET.getlist()])

"""Ajax request. Not working for now. HTML forms should be prepared for it."""
class JsonFilterPostsView(TagYear, ListView):
    """Filter with ajax request"""

    def get_queryset(self):
        queryset = Post.objects.filter(
            Q(date_pub__in=self.request.GET.getlist("date")) |
            Q(categories__in=self.request.GET.getlist("category"))
        ).distinct().values("title", "tags", "slug", "image", "body", "date_pub", "auth")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"posts":queryset}, safe=False)




