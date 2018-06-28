from rest_framework import serializers

from stats.models import Changelog


class changelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Changelog
        fields = ['pk', 'title', 'description', 'date', 'archived']
        read_only_fields = ['pk']

    def validate_title(self, value):
        if(not value):
            raise serializers.ValidationError("The title cannot be empty.")
        return value
