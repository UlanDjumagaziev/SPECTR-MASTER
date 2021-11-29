from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


CREATED = "CREATED"
PENDING = "PENDING"
IN_WAY = "IN_WAY"
DONE = "DONE"

CART_CHOICES = (
    (CREATED, "Created"),
    (PENDING, "Pending"),
    (IN_WAY, "In way"),
    (DONE, "Done")
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=1200)
    description = models.TextField(max_length=1200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    count = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Order(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.CharField(max_length=200)
    done = models.CharField(max_length=100)

# Create your models here.
