from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class FoodProduct(models.Model):
    food_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)

    def __unicode__(self):
        return self.food_name


class Person(models.Model):
    name=models.CharField(max_length=20),
    #birthday=models.DateField(),
    categories=models.ManyToManyField(Category)
    
    def __unicode__(self):
        return self.name
