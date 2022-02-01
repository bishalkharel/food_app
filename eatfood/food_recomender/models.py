from resource import RLIMIT_STACK
from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FoodProduct(models.Model):
    food_name = models.CharField(max_length=100)
    recipe = RichTextField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="food"
    )

    def __str__(self):
        return self.food_name


class Person(AbstractUser):
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category, related_name="category")

    def __str__(self):
        return self.username


class Articel(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Person, on_delete=models.CASCADE, blank=True, null=True, related_name="articles"
    )

    def __str__(self):
        return self.title
