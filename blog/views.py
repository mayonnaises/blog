# blog/views.py

from django.views.generic import (
    ListView,
    TemplateView
)

from .models import Blog


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'
    paginate_by = 20

    def get_queryset(self):
        return Blog.objects.filter(
            is_public=True).order_by('-created_at')

    def get_context_data(self):
        context = super().get_context_data()
        return context


class BlogDetailView(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, pk):
        context = super().get_context_data()
        blog = Blog.objects.get(pk=pk)
        context.update({
            'blog': blog
        })
        return context
