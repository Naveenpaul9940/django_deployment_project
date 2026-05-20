from django.db import models


class Products(models.Model):
    product_id = models.IntegerField(primary_key= True)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
