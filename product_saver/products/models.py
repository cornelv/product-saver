from django.db import models
from django.contrib.postgres.fields import ArrayField


class Supplier(models.Model):

    name = models.CharField(max_length=100)
    url = models.URLField( max_length=256)

    def __str__(self):
        return self.name 

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Product(models.Model):

    name = models.CharField(max_length=100)
    url = models.URLField( max_length=256)

    rating = models.DecimalField(max_digits=5, decimal_places=3)
    reviews = models.PositiveIntegerField()
    positive_reviews = models.PositiveIntegerField()
    orders = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_long = models.CharField(max_length=50, default="", blank=True)

    shipping_options = ArrayField(models.CharField(max_length=200), blank=True)
    epacket_available = models.BooleanField()

    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=None)
    tags = ArrayField(models.CharField(max_length=200), blank=True, default=list)


    def __str__(self):
        return self.name


class Image(models.Model):

    url = models.URLField( max_length=256)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.url
