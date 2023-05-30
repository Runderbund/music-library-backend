from django.urls import path
from .views import song_list, song_detail

urlpatterns = [
    path('music/', song_list, name='music_list'),
    path('music/<int:pk>/', song_detail, name='music_detail'),
]
