from django.db.models.fields import mixins
from rest_framework.serializers import Serializer
from watchlist_app.models import WatchList, StreamPlatform, Reviews
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly

class ReviewsCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Reviews.objects.filter(watchlist=watchlist,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("This Movie is already reviewed")
        
        if watchlist.number_of_ratings == 0:
            watchlist.average_rating = serializer.validated_data['rating']
        else:
            watchlist.average_rating = (watchlist.average_rating + serializer.validated_data['rating'] ) / 2
        watchlist.number_of_ratings = watchlist.number_of_ratings + 1
        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=review_user)
        
    def get_queryset(self):
        return Reviews.objects.all()
        
class ReviewsList(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly ]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)
    
class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [ ReviewUserOrReadOnly ]

# class ReviewsList(mixins.ListModelMixin, 
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewsDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

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
        serializer = WatchListSerializer(watchList)
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