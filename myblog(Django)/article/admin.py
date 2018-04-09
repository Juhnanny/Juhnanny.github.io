from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_time', 'views', 'likes', 'category']
    list_filter = ['title', 'created_time', 'category', 'tags']
    search_fields = ['title', 'category']
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_time']