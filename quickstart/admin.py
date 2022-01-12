from django.contrib import admin
from quickstart.models import Character, Place, Region, Family
# Register your models here.

admin.site.register([Character,Place,Region, Family])