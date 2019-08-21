from django.contrib import admin
from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption'
    )

    list_display = (
        'pk',
        'file',
        'created_at',
        'location',
        'caption',
        'creator'
    )
    #  만든날짜, 이미지 파일, 위치, 설명, 생성자


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at'
    )
    #  내용, 생성자, 이미지, 생성날짜, 수정날짜

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at'
    )
    #  생성자, 이미지, 생성일, 수정일
