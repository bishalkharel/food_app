from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("selectcategory/", views.assign_category),
    path("showitems/", views.show_relatives_items),
    path("login/", views.loginpage, name="login"),
    path("logout/", views.logoutpage, name="logout"),
    path("signup/", views.signup_page, name="signup"),
    path("recipes/", views.recipe_page, name="recipes"),
    path("recipe_detail/<int:id>", views.recipe_detail, name="recipe_detail"),
    path("articles/", views.all_articles, name="all_articles"),
    path("article_detail/<int:id>", views.article_detail, name="article_detail"),
    path("search/", views.search, name="search"),
]
