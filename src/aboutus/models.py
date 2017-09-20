# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _

class ChairPersonsRemarks(models.Model):
	remarks = models.TextField(_("Chair Person's Remarks"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "CHAIRPERSON'S REMARK"
		verbose_name_plural = "CHAIRPERSON'S REMARKS"

	def __unicode__(self):
		return self.remarks

class WhoWeAre(models.Model):
	who_we_are = models.TextField(_("Who we Are"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "WHO WE ARE"
		verbose_name_plural = "WHO WE ARE"

	def __unicode__(self):
		return self.who_we_are

class OurVision(models.Model):
	vision = models.TextField(_("Our Vision"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "OUR VISION"
		verbose_name_plural = "OUR VISIONS"

	def __unicode__(self):
		return self.vision

class OurMainObjective(models.Model):
	objective = models.TextField(_("Our Main Objective"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "OUR MAIN OBJECTIVE"
		verbose_name_plural = "OUR MAIN OBJECTIVES"

	def __unicode__(self):
		return self.objective

class OurTeam(models.Model):
	team = models.TextField(_("Our Team"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "OUR TEAM"
		verbose_name_plural = "OUR TEAMS"

	def __unicode__(self):
		return self.team

class Careers(models.Model):
	caree = models.TextField(_("Careers"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "CAREER"
		verbose_name_plural = "CHAREERS"

	def __unicode__(self):
		return self.caree

class ContactUs(models.Model):
	contact = models.TextField(_("Contact us"), null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = "CONTACT US"
		verbose_name_plural = "CONTACT US"

	def __unicode__(self):
		return self.contact
# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    message = models.TextField(_("Message"), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "CONTACT FORM"
        verbose_name_plural = "CONTACT FORMS"

    def __unicode__(Self):
        return self.email
