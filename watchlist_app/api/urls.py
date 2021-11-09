from django.urls import path
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('movie/<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),
]