# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin
from .models import Graphs, Resources
# Register your models here.

class ResourcesAdmin(admin.ModelAdmin):
	list_display = ['resource_name', 'resource_link', 'resource_type', 'created']
	list_filter = ('resource_name', 'resource_link', 'resource_type', 'created',)
	search_fields = ('resource_name', 'resource_link', 'resource_type',)

	class Meta:
		model = Resources

admin.site.register(Resources, ResourcesAdmin)


class GraphsAdmin(admin.ModelAdmin):
	list_display = ['title','year','created']
	list_filter = ('title', 'year',)
	search_fields = ('title', 'year',)

	class Meta:
		model = Graphs

admin.site.register(Graphs, GraphsAdmin)



