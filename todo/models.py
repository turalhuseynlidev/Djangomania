from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#THIRD PARTY modules:
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category_view',
            kwargs={
            'category_slug': self.slug
            }
        )
    
class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'tag_view',
            kwargs={
            'tag_slug': self.slug
            }
        )


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #bu user silinerse, onun yaratdigi todo-lar da silinecekdir.
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # Category = models.ForeignKey(Category, on_delete=models.CASCADE) #bu kateqoriya silinerse o kateqoriyaya aid olan butun todo-lar silinecekdir.
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'todo_detail_view',
            kwargs={
            'category_slug': self.category.slug,
            'id': self.pk
            }
        )
