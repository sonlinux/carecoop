# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Frequently Asked Questions
class FrequentlyAskQuestions(models.Model):
	question = models.CharField(_('Question'),max_length=255, null=True, blank=True)
	answer = models.CharField(_('Answer'), max_length=255, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class meta:
		ordering = ['-created']
		verbose_name = 'F.A.Q'
		verbose_name_plural = 'F.A.Qs'

	def __unicode__(self):
		return self.question
