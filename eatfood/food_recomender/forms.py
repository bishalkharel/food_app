from django import forms
from .models import Person
from food_recomender.models import Category

class CustomMMCF(forms.ModelMultipleChoiceField): # multiple choice option ko lagi 
    def label_from_instance(self, category):
        return f"{category.name}"
        
        
class CreatePersonForm(forms.ModelForm):
     class Meta:
            model = Person
            fields = ['categories']    

         
     categories = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )