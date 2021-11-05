from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    movies_values = movies.values()
    # print("movies_values is ",movies_values)
    list_movies_values = list(movies_values)
    # print("list_movies_values is ",list_movies_values)
    data = {'movies' : list_movies_values }
    return JsonResponse(data)

def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    data = {'movie':movie.name}
    return JsonResponse(data)
