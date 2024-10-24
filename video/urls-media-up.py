from django.urls import path
from django.conf import settings
from .views import media_upload

from . import views

urlpatterns = [
    path('', views.video, name='video'),
    path('media_upload', media_upload, name='media_upload'),
]