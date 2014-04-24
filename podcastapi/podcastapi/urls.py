from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from podcasts import views


admin.autodiscover()

router = routers.DefaultRouter()
router.register(
    r'podcast', views.PodcastViewSet,
)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # Rest framework urls
    url(r'^api/v1/', include(router.urls)),
    # swagger docs url
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
