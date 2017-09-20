# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
'''
PhotoGallery model having Event name, image, hits(views) and description
'''

class PhotoGallery(models.Model):
	image = models.ImageField(upload_to='images%Y/%m/%d')
	event_name = models.CharField(_('Event Name'),max_length=255, null=True, blank=True)
	hits = models.IntegerField(null=True, blank=True)
	comments = models.IntegerField(null=True, blank=True)
	description = models.TextField(_('Discription'), null=True, blank=True)
	created = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'PHOTO GALLERY'
		verbose_name_plural = 'PHOTO GALLERIES'


	def __unicode__(self):
		return self.event_name

'''
News letter model having news file (pdf) and details
'''

class NewsLetter(models.Model):
	title = models.CharField(_('Title'), max_length=255, null=True, blank=True)
	body = models.TextField(_('Body'), null=True, blank=True)
	created = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created"]
		verbose_name = 'NEWS LETTER'
		verbose_name_plural = 'NEWS LETTERS'

	def __unicode__(self):
		return self.details

'''
Success Stories having Text, Title and Image
'''
class SuccessStories(models.Model):
	image = models.ImageField(upload_to='images%Y/%m/%d')
	title = models.CharField(_('Title'), max_length=255, null=True, blank=True)
	authur = models.CharField(_('Authur'), max_length=255, null=True, blank=True)
	story = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'SUCCESS STORY'
		verbose_name_plural = 'SUCCESS STORIES'

	def __unicode__(self):
		return self.title
