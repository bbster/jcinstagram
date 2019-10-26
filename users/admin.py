from django.contrib import admin
from django.contrib.admin import ModelAdmin
from users.models import User


@admin.register(User)
class MemberAdmin(ModelAdmin):
    list_display = ('id',
                    'username',
                    'password',
                    'first_name',
                    'last_name',
                    'bio',
                    'website',
                    'phone',
                    'gender'
                    )
