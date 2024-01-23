from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('drinks/', views.drinks, name='drinks'),
    path('food/', views.food, name='food'),
    path('calculator/', views.calculator, name='calculator'),
]