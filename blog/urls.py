# blog/urls.py

from django.urls import path

from .views import (
    BlogDetailView,
    BlogsFilteredByTag,
    BlogListView,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('tag/<slug:tag_pk>/', BlogsFilteredByTag.as_view(), name='blogs_filtered_by_tag'),
    path('<slug:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]