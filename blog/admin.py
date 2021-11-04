from django.contrib import admin

from .models import Blog, Group, Tag


admin.site.register(Blog)
admin.site.register(Group)
admin.site.register(Tag)