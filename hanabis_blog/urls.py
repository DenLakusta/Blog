from django.contrib.flatpages.views import flatpage
from django.urls import path
from django.contrib.flatpages import views
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
    path('authors/<slug:slug>/', views.AuthorDetailView.as_view(), name="author_detail"),
    path('<slug:slug>/', views.TagDetailView.as_view(), name="tag_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
    path('filter/', views.FilterPostsView.as_view(), name='filter'),
    path('json_filter/', views.JsonFilterPostsView.as_view(), name='json_filter'),
    path('about/', flatpage, name='about'),
    path('contact/', flatpage, name='contact'),
    path('accounts/logout/', TemplateView.as_view(template_name='account/logout.html'))
]