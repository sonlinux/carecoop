from __future__ import absolute_import

from django.conf.urls import url
from .views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='index'),
]
