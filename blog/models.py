# blog/models.py
import uuid

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_tag'


class Group(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_group'


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    icon = models.ImageField(
        upload_to='blog_icon/',
        blank=True,
        null=True,
        verbose_name='main_image',
    )
    content = models.TextField()
    description = models.TextField(
        'article description',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='group_of'
    )
    is_published = models.BooleanField(
        'public status',
        default=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_blog'