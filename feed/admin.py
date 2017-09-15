from django.contrib import admin
from feed.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "timestamp",
        "body",
        "category",
        "author"
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
