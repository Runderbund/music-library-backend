from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

# As a developer, I want to create a GET endpoint the responds with a 200 success status code and all of the songs within the Music table.  
    # return Response(serializer.data, status=status.HTTP_200_OK) is equivalent to return Response(serializer.data). Default is 200.

