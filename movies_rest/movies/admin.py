from django.contrib import admin

# Register your models here.
from .models import Person, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
