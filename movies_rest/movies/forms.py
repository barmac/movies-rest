from django import forms

from .models import Movie, Person


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'