# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (ChairPersonsRemarks, WhoWeAre, OurVision, OurMainObjective, OurTeam, Careers)

class ChairPersonsRemarksAdmin(admin.ModelAdmin):
	list_display = ['remarks']

	class Meta:
		model = ChairPersonsRemarks

admin.site.register(ChairPersonsRemarks, ChairPersonsRemarksAdmin)

class WhoWeAreAdmin(admin.ModelAdmin):
	list_display = ['who_we_are']

	class Meta:
		model = WhoWeAre

admin.site.register(WhoWeAre, WhoWeAreAdmin)

class OurVisionAdmin(admin.ModelAdmin):
	list_display = ['vision']

	class Meta:
		model = OurVision

admin.site.register(OurVision, OurVisionAdmin)

class OurMainObjectiveAdmin(admin.ModelAdmin):
	list_display = ['objective']

	class Meta:
		model = OurMainObjective

admin.site.register(OurMainObjective, OurMainObjectiveAdmin)

class OurTeamAdmin(admin.ModelAdmin):
	list_display = ['team']

	class Meta:
		model = OurTeam

admin.site.register(OurTeam, OurTeamAdmin)

class CareersAdmin(admin.ModelAdmin):
	list_display = ['caree']

	class Meta:
		model = Careers

admin.site.register(Careers, CareersAdmin)

# class ContactUsAdmin(admin.ModelAdmin):
# 	list_display = ['full_name', 'email', 'created']
#
# 	class Meta:
# 		model = ContactUs
#
# admin.site.register(ContactUs, ContactUsAdmin)

# Register your models here.
