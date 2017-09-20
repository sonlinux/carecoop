# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Members(models.Model):
    name = models.CharField(_('Name'),max_length=255, null=True, blank=True)
    position = models.CharField(_('Position'), max_length=255, null=True, blank=True)
    organization = models.CharField(_('Organization'), max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(_("Image"), upload_to='images%Y/%m/%d',null=True, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'MEMBER'
        verbose_name_plural = 'MEMBERS'
        
    def __unicode__(self):
        return self.name



"""
Chairpersons' Introductory Remarks
"""
class ChairRemarks(models.Model):
    name = models.ForeignKey(Members)
    text = models.TextField(_("Text"), null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'CHAIRPERSONS'
        verbose_name_plural = 'CHAIRPERSONS'

    def __unicode__(self):
        return self.name
"""
    Layout for the model of Supervisory Committe
    This will include an image, names, positions and nationality 
"""
class SupervisoryCommittee(models.Model):
    name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
    position = models.CharField(_('Position on Board'), max_length=255, null=True, blank=True)    
    nationality = models.CharField(_('Nationality'), max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'SUPERVISORY COMMITTEE'
        verbose_name_plural ='SUPERVISORY COMMITTEES'

    def __unicode__(self):
        return self.name

# class GovernanceOfCarecoop(model.Model):
class LoansCommittee(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
  
    

