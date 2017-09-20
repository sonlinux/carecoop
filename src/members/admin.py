# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin
from .models import Members, SupervisoryCommittee
from .models import Members, ChairRemarks 

class MembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'organization']
    list_filter = ('name', 'position', 'organization',)
    search_fields = ('name', 'position', 'organization',)

    class Meta:
        model = Members

admin.site.register(Members, MembersAdmin)

class SupervisoryCommitteeAdmin(admin.ModelAdmin):
	list_display = ['name', 'position', 'nationality']
	list_filter = ('name',)
	search_fields = ('name',)

	class Meta:
		model = SupervisoryCommittee
		
admin.site.register(SupervisoryCommittee, SupervisoryCommitteeAdmin)


class ChairRemarksAdmin(admin.ModelAdmin):
	list_display = ["name", "text"]
	
	class Meta:
		model = ChairRemarks

admin.site.register(ChairRemarks, ChairRemarksAdmin)


