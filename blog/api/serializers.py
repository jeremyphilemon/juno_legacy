from rest_framework import serializers

from blog.models import Story


class storySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Story
        fields = ['url', 'pk', 'title', 'story', 'date', 'archived']
        read_only_fields = ['url', 'pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        if(not value):
            raise serializers.ValidationError("The title cannot be empty.")
        return value
