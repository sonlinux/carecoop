from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _ 

'''
Graph class defines properties of graphs that are to be implemented on the website
'''
class Graphs(models.Model):

	title = models.CharField(_('Graph_title'), max_length = 255, null= True, blank= True)
	year = models.DateField(default = timezone.now)
	link = models.TextField(_('graph_link'), null = True)
	created = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'GRAPH'
		verbose_name_plural = 'GRAPHS'

	def __encode__(self):
		return self.title

'''
Resource class defines different resource types all distinguished
from each other with the use of the resource_type field that acts as a foreign key
'''
class Resources(models.Model):
	resource_name = models.CharField(_('Resource_name'), max_length = 255, blank = False)
	resource_link = models.TextField(_('Resource_link'))
	resource_type = models.CharField(_('Resource_type'), max_length = 255, blank = False)
	created = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'RESOURCE'
		verbose_name_plural = 'RESOURCES'

	def __unicode__(self):
		return self.resource_name


