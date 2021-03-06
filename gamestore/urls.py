"""gamestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from users.views import user_api_view, user_register_view, user_login_view

router = routers.DefaultRouter()
router.register(r'games', views.VideoGameViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', user_api_view, name='user_api'),
    path('users/register', user_register_view, name='register'),
    path('users/login', user_login_view, name='login')
]
