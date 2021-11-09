from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class WatchListAV(APIView):

    def get(self,request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)       

class WatchDetailAV(APIView):
    def get(self, request,pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(WatchList)
        return Response(serializer.data)

    def put(self, request,pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request,pk):
        watchList = WatchList.objects.get(pk=pk)
        WatchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):

    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)       

class StreamPlatformDetailAV(APIView):
    def get(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)