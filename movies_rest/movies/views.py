from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import MovieSerializer
from .models import Movie

# Create your views here.


class MoviesView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):

    def get_object(self, id):
        try:
            movie = Movie.objects.get(id=id)
            return movie
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = self.get_object(id=id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id):
        movie = self.get_object(id=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = self.get_object(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
