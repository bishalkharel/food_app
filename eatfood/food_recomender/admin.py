from cProfile import label
from django.contrib import admin

from .models import Category,FoodProduct,Person

class AdminPerson(admin.ModelAdmin):
    label=['name','categories']

class AdminCategory(admin.ModelAdmin):
    label=['name']

class AdminFoodproduct(admin.ModelAdmin):
    label=['food_name','category']

admin.site.register(Category,AdminCategory)
admin.site.register(FoodProduct,AdminFoodproduct)
admin.site.register(Person,AdminPerson)

