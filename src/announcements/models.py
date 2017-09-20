# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Announcements(models.Model):
	title = models.CharField(_("Title"), max_length=40, null=True, blank=True)
	image = models.ImageField(_("Images"), upload_to='images%Y/%m/%d', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	details = models.TextField(_("Details"), null=True, blank=True)
	venues = models.CharField(_("venues"), max_length=40, null=True, blank=True)

	class Meta:
		ordering =['-created']
		verbose_name = 'ANNOUCEMENT'
		verbose_name_plural = 'ANNOUNCEMENTS'

	def __unicode__ (self):
		return self.name 