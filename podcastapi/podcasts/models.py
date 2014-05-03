from django.db import models


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    feed_url = models.URLField(unique=True)

    image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=255, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, related_name='episodes')
    guid = models.CharField(max_length=512, unique=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    published_on = models.DateTimeField()

    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)
