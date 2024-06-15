from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.home_page, name="home"),
]
