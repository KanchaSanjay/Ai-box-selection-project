from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=50)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    max_weight = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
