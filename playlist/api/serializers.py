from rest_framework import serializers

from playlist.models import Song


class playlistSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ['url', 'pk', 'title', 'description', 'date', 'location', 'art', 'archived']
        read_only_fields = ['url', 'pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        if(not value):
            raise serializers.ValidationError("The title cannot be empty.")
        return value
