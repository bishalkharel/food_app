
from xml.etree.ElementInclude import include
from django.shortcuts import render,redirect
from .forms import CreatePersonForm
from .models import Person,Category,FoodProduct


def assign_category(request):
    if request.method == "POST":
        form = CreatePersonForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            foods = []
            for category in form.cleaned_data.get("categories"):
                foods.extend(category.food.all())
            return render(request,'show_items.html',{"foods":foods})
    form=CreatePersonForm()
    return render(request, "selectcategory.html", {"form": form})

def show_relatives_items(request):
    if request.user.is_authenticated:
        print(request.post)
        items=Person.objects.get(id=request.user.id).categories.values("name",)
        items_available={
            "items":items
        }
        return render(request,'website-menu-06/index.html',items_available)
    return redirect('')
    

