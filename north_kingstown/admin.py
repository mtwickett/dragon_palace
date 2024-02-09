from django.contrib import admin
from .models import Drink

# Register your models here.

@admin.register(Drink) 
class DrinkAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)