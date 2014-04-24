from rest_framework import serializers

from .models import Podcast, PodcastEpisode


class PodcastEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastEpisode
        fields = (
            'id',
            'title',
            'url',
            'published_on',
            'description',
            'author',
        )


class PodcastSerializer(serializers.ModelSerializer):
    episodes = PodcastEpisodeSerializer(many=True)

    class Meta:
        model = Podcast
        fields = (
            'id',
            'title',
            'feed_url',
            'image_url',
            'description',
            'author',
            'link',
            'episodes',
        )
