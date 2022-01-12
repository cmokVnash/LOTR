"""LOTR_Family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from quickstart import views
from rest_framework import routers

router = routers.DefaultRouter()
#r means raw string Python raw string treats backslash (\) 
# as a literal character. 
# This is useful when we want to have a string that 
# contains backslash and don’t want it to be treated as 
# an escape character.
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'characters',views.CharacterViewSet)
router.register(r'region',views.RegionViewSet)
router.register(r'place',views.PlaceViewSet)
router.register(r'characterlist',views.showPlaceViewSet, basename='char')

urlpatterns = [
    path('',include(router.urls)),
    #REST framework's login and logout views
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
