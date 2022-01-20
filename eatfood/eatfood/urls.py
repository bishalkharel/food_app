
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from food_recomender import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('selectcategory/',views.assign_category)
]
