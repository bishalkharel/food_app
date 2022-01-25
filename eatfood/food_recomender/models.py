from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FoodProduct(models.Model):
    food_name=models.CharField(max_length=100)
    recepie=models.TextField(max_length=300)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True,related_name="food")

    def __str__(self):
        return self.food_name


class Person(AbstractUser):
    name=models.CharField(max_length=20)
    categories=models.ManyToManyField(Category,related_name="category")
    def __str__(self):
        return self.name
