from django.urls import path
from .views import song_list, song_detail, song_create, song_like

urlpatterns = [
    path('music/', song_list, name='music_list'),
    path('music/create/', song_create, name='song_create'),
    path('music/<int:pk>/', song_detail, name='song_detail'),
    path('music/<int:pk>/like/', song_like, name='song_like'),
]
