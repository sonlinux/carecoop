# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PhotoGallery, NewsLetter, SuccessStories

# Multimedia models
class PhotoGalleryAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'image', 'hits', 'comments', 'description']
	list_filter = ('event_name',)
	search_fields = ('event_name',)

	class Meta:
		model = PhotoGallery

admin.site.register(PhotoGallery, PhotoGalleryAdmin)

class NewsLetterAdmin(admin.ModelAdmin):
	list_display = ['title']
	list_filter = ('title', 'body', 'created',)
	search_fields = ('title', 'body', 'created',)

	class Meta:
		model = NewsLetter

admin.site.register(NewsLetter, NewsLetterAdmin)

class SuccessStoriesAdmin(admin.ModelAdmin):
	list_display = ['title', 'authur', 'story']
	list_filter = ('title', 'authur',)
	search_fields = ('title', 'authur',)

	class Meta:
		model = SuccessStories

admin.site.register(SuccessStories, SuccessStoriesAdmin)
