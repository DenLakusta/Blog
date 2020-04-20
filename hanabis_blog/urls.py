from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
    path('authors/<slug:slug>/', views.AuthorDetailView.as_view(), name="author_detail"),
    path('<slug:slug>/', views.TagDetailView.as_view(), name="tag_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review")
]