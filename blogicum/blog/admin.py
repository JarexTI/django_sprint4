from django.contrib import admin

from .models import Category, Comment, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category'
    )

    search_fields = (
        'title',
        'text',
    )

    list_filter = (
        'pub_date',
        'author',
        'location',
        'category'
    )

    empty_value_display = 'Не задано'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug'
    )

    list_filter = (
        'title',
        'slug'
    )

    empty_value_display = 'Не задано'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    list_filter = (
        'name',
    )

    empty_value_display = 'Не задано'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'author',
        'created_at'
    )

    search_fields = (
        'author',
    )

    empty_value_display = 'Не задано'
