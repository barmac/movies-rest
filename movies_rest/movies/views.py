from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.views import APIView, Response

from .forms import MovieForm
from .serializers import MovieSerializer, PersonSerializer
from .models import Movie, Person


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

    def get_object(self, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return movie

    def get(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeopleView(APIView):

    def get(self, request):
        movies = Person.objects.all()
        serializer = PersonSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):

    def get_object(self, pk):
        movie = get_object_or_404(Person, pk=pk)
        return movie

    def get(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = PersonSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = PersonSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseView(View):

    def get(self, request):
        form = MovieForm
        ctx = {
            "form": form
        }
        return render(request, "movies/content.html", ctx)
