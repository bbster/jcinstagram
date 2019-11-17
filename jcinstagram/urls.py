from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('images/', include('images.urls')),
    path('notifications/', include('notifications.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
]
