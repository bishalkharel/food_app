from django.shortcuts import render,redirect
from .forms import CreatePersonForm
from .models import Person,Category,FoodProduct



def assign_category(request):
    if request.method == "POST":
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            categ_form = form.update(commit=False)
            categ_form.user = request.user
            categ_form.save()
    form=CreatePersonForm()
    return render(request, "selectcategory.html", {"form": form})


def show_relatives_items(request):
    if request.user.is_authenticated:
        items=Person.objects.get(id=request.user.id)
        print((items.values_list))
        items_available={
            "items":items
        }
        return render(request,'show_items.html',items_available)
    return redirect('')

