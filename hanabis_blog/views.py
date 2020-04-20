from django.shortcuts import render, redirect
from  .forms import ReviewForm
# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Post, Tag, Author


# class PostsView(ListView):
#     model = Post
#     queryset = Post.objects.filter(draft=False)
# #

class PostsView(ListView):
    post_list = Post
    queryset = Post.objects.filter(draft=False)



class TagView(View):

    def get(self, requests):
        tags = Tag.objects.all()
        return render(requests, 'tags/tags_list.html', {'tags_list':tags})
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
            print(form.post_id)
            form.save()
        return redirect(post.get_absolute_url())


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'hanabis_blog/author_detail.html'
    slug_field = "slug"

class TagDetailView(ListView):
    model = Tag
    slug_field = "slug"
