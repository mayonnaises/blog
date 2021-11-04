# blog/views.py

from django.views.generic import (
    ListView,
    TemplateView
)

from .models import Blog, Tag


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'
    paginate_by = 20

    def get_queryset(self):
        return Blog.objects.filter(
            is_published=True
        ).order_by('-created_at').defer('content')

    def get_context_data(self):
        context = super().get_context_data()
        return context


class BlogDetailView(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_blog(self, pk):
        blog = Blog.objects.select_related(
                'group'
            ).prefetch_related(
                'tags'
            ).get(pk=pk)
        return blog

    def get_related_posts(self, uid, group):
        related_posts = Blog.objects.filter(
                group=group
            ).exclude(
                id=uid
            ).defer('content')
        return related_posts

    def get_context_data(self, pk):
        context = super().get_context_data()

        blog = self.get_blog(pk)

        if (group := blog.group) is not None:
            related_posts = self.get_related_posts(blog.id, group)
            if len(related_posts) > 1:
                context.update({
                    'related_posts': related_posts
                })

        context.update({
            'blog': blog
        })
        return context


class BlogsFilteredByTag(ListView):
    template_name = 'blog/blogs_filtered_by_tag.html'
    context_object_name = 'blog_list'
    paginate_by = 20

    def get_queryset(self):
        return Blog.objects.filter(
            tags__pk=self.kwargs['tag_pk'],
            is_published=True
        ).order_by('created_at').defer('content')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'tag': Tag.objects.get(pk=self.kwargs['tag_pk'])
        })
        return context