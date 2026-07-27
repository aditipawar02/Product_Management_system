from django.db import models

# Create your models here.

class Product( models.Model ) :
    name = models.CharField( max_length=50 )
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField( max_length=50 )
    image = models.ImageField(upload_to='Product/', blank=True, null=True)

def __str__(self):
        return f" {self.name} - {self.price} - {self.quantity} - {self.category}"