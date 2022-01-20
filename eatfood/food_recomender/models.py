from django.db import models


class Person(models.Model):
    name=models.CharField(max_length=20),
    birthday=models.DateField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FoodProduct(models.Model):
    food_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.food_name
