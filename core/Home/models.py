from django.db import models

# Create your models here.


class Students(models.Model):
    
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    email = models.EmailField( max_length=254)
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class Cars(models.Model):
    car_name =models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
