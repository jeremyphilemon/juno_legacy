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


class playlistRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Song.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
