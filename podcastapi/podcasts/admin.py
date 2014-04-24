from django.contrib import admin

from .models import Podcast, PodcastEpisode


class PodcastEpisodeInline(admin.StackedInline):
    model = PodcastEpisode


class PodcastAdmin(admin.ModelAdmin):
    inlines = [
        PodcastEpisodeInline,
    ]


admin.site.register(PodcastEpisode)
admin.site.register(Podcast, PodcastAdmin)
