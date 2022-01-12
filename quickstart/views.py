from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import renderer_classes
#
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets

from rest_framework.response import Response
# Create your views here.

from django.contrib.auth.models import User, Group
from quickstart.models import Character, Place, Region
from rest_framework import viewsets, permissions
from quickstart.serializers import UserSerializers, GroupSerializers, CharacterSerializers, RegionSerializers, PlaceSerializers

#viewsets are controllers they do not use method handlers like get or post as is used with function based api's using the decorator @
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializers
    permission_classes = [permissions.IsAuthenticated]

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializers
    permission_classes = [permissions.IsAuthenticated]

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializers
    permission_classes = [permissions.IsAuthenticated]

class showPlaceViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'characters.html'
    
    def list(self, request):
        queryset = Character.objects.all()
        serializer = RegionSerializers(queryset, many=True , context={'request': request})
        return Response({'regions': queryset})#(serializer.data)