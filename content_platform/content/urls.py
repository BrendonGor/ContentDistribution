# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='blog_index'),  # The main page of the blog
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # A detail view of a blog post
]
