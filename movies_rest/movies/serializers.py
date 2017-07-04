from rest_framework import serializers
from .models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedRelatedField(view_name='person_detail', read_only=True)
    actors = serializers.HyperlinkedRelatedField(view_name='person_detail', read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('director', 'actors')
