from django.db import models
from django.db.models.deletion import SET_NULL
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.





class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000 , null=True, blank=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region,null=True,blank=True, on_delete=SET_NULL)
    description = models.TextField(max_length=1000 , null=True, blank=True)

    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000 , null=True, blank=True)
    

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True )
    region = models.ForeignKey(Region,null=True, blank=True, on_delete=SET_NULL)
    # When you are giving a related_name to a OneToOne(or ForeignKey Field), it will give the related object, 
    # for example in the model the previous post,
    # a reference to current post. 
    # So when we type previous_post.next, it will return current post.
    family = models.ForeignKey(Family,null=True, blank=True, on_delete=SET_NULL)
    parents = models.ManyToManyField('self')
    previous = models.ForeignKey('self', blank=True, null=True, on_delete=SET_NULL, related_name='next')
    generation = models.IntegerField( null=True, blank=True, validators=[MaxValueValidator(9),MinValueValidator(1)])
    description = models.TextField(max_length=1000 , null=True, blank=True)
    

    def __str__(self):
        return self.name

