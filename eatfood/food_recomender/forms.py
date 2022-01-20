from os import name
from django import forms
from .models import Person
from food_recomender.models import Category

class CustomMMCF(forms.ModelMultipleChoiceField): # multiple choice option ko lagi 
    def label_from_instance(self, category):
        return “%s” % category.name
        
        
class CreateMealForm(forms.ModelForm):
        class Meta:
            model = Person
            fields = ['name', 'birthday','choose_categories']    

    name = forms.CharField()
    date = forms.DateInput()    
    choose_categories = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )