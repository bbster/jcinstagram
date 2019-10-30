from django.contrib import admin
from django.contrib.admin import ModelAdmin
from users.models import User


@admin.register(User)
class MemberAdmin(ModelAdmin):
    list_display = ('id',
                    'username',
                    'password',
                    'profile_image',
                    'first_name',
                    'last_name',
                    'bio',
                    'website',
                    'phone',
                    'gender'
                    )
