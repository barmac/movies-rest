from django.shortcuts import render
from rest_framework.views import APIView, Response

from .serializers import MovieSerializer
from .models import Movie

# Create your views here.


class MoviesView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, context={"request": request})
        return Response(serializer.data)
