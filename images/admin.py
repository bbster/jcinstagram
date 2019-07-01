from django.contrib import admin
from django.contrib.admin import ModelAdmin
from images.models import Image, Comment


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ('id', 'file', 'location', 'caption', 'created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'message', 'created_at', 'updated_at')