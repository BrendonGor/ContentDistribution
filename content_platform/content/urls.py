# blog/urls.py

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

meta_data_router = DefaultRouter()
# base_name is automatically the model name (lowercase) associated with  the queryset
meta_data_router.register(r"subjects", views.SubjectViewSet)
meta_data_router.register(r"courses", views.CourseViewSet)
meta_data_router.register(r"topics", views.TopicViewSet)

urlpatterns = [
    # path('', views.index, name='blog_index'),  # The main page of the blog
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # A detail view of a blog post
]
urlpatterns += meta_data_router.urls

# https://www.django-rest-framework.org/api-guide/routers/
# for viewsets it goes instance, app, base name
