# blog/urls.py

from django.urls import path

from .views import (
    BlogDetailView,
    BlogListView
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]