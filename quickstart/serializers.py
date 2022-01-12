from django.contrib.auth.models import User, Group
from rest_framework import fields, serializers
from quickstart.models import Character, Place, Region
#when retrieving data
class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        #use model for which data will be retrieved
        model = User
        fields = ['url','username','email','groups']

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CharacterSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['url', 'name', 'title']

class RegionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['url', 'name']

class PlaceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['url', 'name']