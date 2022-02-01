from django.shortcuts import render, redirect
from .forms import CreatePersonForm
from .models import Person, Category, FoodProduct
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import random


def assign_category(request):
    if request.method == "POST":
        form = CreatePersonForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            foods = []
            for category in form.cleaned_data.get("categories"):
                foods.extend(category.food.all())
            return render(request, "show_items.html", {"foods": foods})
    if request.user.categories.exists():
        foods = []
        for category in request.user.categories.all():
            foods.extend(category.food.all())
        return render(request, "show_items.html", {"foods": foods})

    form = CreatePersonForm()
    return render(request, "selectcategory.html", {"form": form})


def show_relatives_items(request):
    if request.user.is_authenticated:
        print(request.post)
        items = Person.objects.get(id=request.user.id).categories.values(
            "name",
        )
        items_available = {"items": items}
        return render(request, "website-menu-06/index.html", items_available)
    return redirect("")


def home(request: HttpRequest):
    foods = FoodProduct.objects.all()
    if request.user.is_authenticated:
        categories = request.user.categories.all()
        foods = [category.food.all() for category in categories]
        foods = [j for i in foods for j in i]
    random_food = random.choice(foods)
    return render(
        request,
        "index.html",
        context={"foods_home": foods[:2], "foods": foods, "random_food": random_food},
    )


def loginpage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return redirect("login")

    return render(request, "registration/login.html")


def logoutpage(request):
    logout(request)
    return redirect("login")


def signup_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("home")

    foods = Category.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            if len(password2) >= 8:
                try:
                    person = Person.objects.get(username=username, password=password)
                    if person.username == username:
                        messages.error(request, "Username already exists")
                        return redirect("signup")
                except Person.DoesNotExist:
                    person = Person.objects.create_user(
                        username=username, password=password
                    )
                    for i in foods:
                        if request.POST.get(str(i.id)):
                            person.categories.add(i)
                    return redirect("signup")
            else:
                messages.error(request, "Password must be at least 8 characters")
                return redirect("signup")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("signup")
    return render(request, "registration/signup.html", context={"foods": foods})


def recipe_page(request: HttpRequest):
    foods = FoodProduct.objects.all()

    random_food = random.choice(foods)

    return render(
        request,
        "all_recipes.html",
        context={"foods": foods, "random_food": random_food},
    )


def recipe_detail(request, id):
    food = FoodProduct.objects.get(id=id)
    return render(
        request,
        "recipe_detail.html",
        context={
            "food": food,
        },
    )
