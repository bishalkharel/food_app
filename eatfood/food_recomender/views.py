from django.shortcuts import render
from .forms import CreatePersonForm



def assign_category(request):
    if request.method == "POST":
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            categ_form = form.save(commit=False)
            categ_form.user = request.user
            categ_form.save()
    form=CreatePersonForm()
    return render(request, "selectcategory.html", {"form": form})

