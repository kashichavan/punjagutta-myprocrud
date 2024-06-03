from django.db import models

# Create your models here.

class CarModel(models.Model):
    name=models.CharField(max_length=25)
    price=models.FloatField()
    photo=models.ImageField(upload_to='media/')

