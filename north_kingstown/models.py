from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=50)
    alcohol = models.CharField(max_length=50)
    bottle_size = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self): 
        return self.name