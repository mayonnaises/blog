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
    description = models.TextField(
        'タグの説明',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


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
        null=True
    )
    content = models.TextField()
    description = models.TextField(
        '記事の説明',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    is_public = models.BooleanField(
        '公開ステータス',
        default=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title