# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FrequentlyAskQuestions

class FrequentlyAskQuestionsAdmin(admin.ModelAdmin):
	list_display = ['question', 'answer', 'created']
	list_filter = ('question',)
	search_fields = ('question',)

	class Meta:
		model = FrequentlyAskQuestions

admin.site.register(FrequentlyAskQuestions, FrequentlyAskQuestionsAdmin)
