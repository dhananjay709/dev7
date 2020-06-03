from django.urls import include, path
from django.conf.urls import url
from .views import *

app_name = 'api-users'

urlpatterns = [
    url(r'^$', UserAPIView.as_view()),
    url(r'^(?P<id>[\w-]+)/$', UserDetailAPIView.as_view()),

    url(r'^activity_period/$', UserAPIView.as_view()),
    url(r'^activity_period/(?P<id>[\w-]+)/$', ActivityPeriodDetailAPIView.as_view()),
]