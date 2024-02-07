from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('drink/', views.drink, name='drink'),
    path('food/', views.food, name='food'),
    path('calculator/', views.calculator, name='calculator'),
]