from django.urls import path
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV, StreamPlatformDetailAV, ReviewsList, ReviewsDetail, ReviewsCreate

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('movie/<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),
    
    path('stream/<int:pk>/review',ReviewsList.as_view(),name='reviews-list'),
    path('stream/<int:pk>/review-create',ReviewsCreate.as_view(),name='reviews-create'),

    path('stream/review/<int:pk>',ReviewsDetail.as_view(),name='review-detail')
    # path('review',ReviewsList.as_view(),name='reviews-list'),
    # path('review/<int:pk>',ReviewsDetail.as_view(),name='review-detail')
]