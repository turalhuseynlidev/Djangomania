from django.contrib import admin
from .models import Todo, Category, Tag
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'is_active',
    ]

class TagAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'is_active',
    ]

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'category',
        'title',
        'is_active',
        'content',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'pk',
        'category',
        'title'
    ]

admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
