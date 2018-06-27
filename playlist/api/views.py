from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from playlist.api.serializers import playlistSerializer
from playlist.models import Song


class playlistCLS(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        playlist = Song.objects.filter(archived=False).order_by('-date')
        return playlist

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)