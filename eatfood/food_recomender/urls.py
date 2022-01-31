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
]
