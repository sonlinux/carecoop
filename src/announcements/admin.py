from __future__  import absolute_import
from __future__  import unicode_literals
from django.contrib import admin
from .models import Announcements

# Register your models here.
class AnnouncementsAdmin(admin.ModelAdmin):
	list_display = ['title', 'venues', 'image','details', 'created']
	list_filter = ('title', 'venues', 'image','details',)
	search_fields = ('title', 'venues', 'image','details',)

	class Meta:
		model = Announcements

admin.site.register(Announcements, AnnouncementsAdmin)
