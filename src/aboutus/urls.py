from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.AboutUsView.as_view(), name="about"),
    url(r"^contact/", views.ContactUsCreateView.as_view(), name="contact"),
]
