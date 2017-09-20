# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from . import models
from .forms import ContactUsForm
from django.core.urlresolvers import reverse_lazy
# from .models import aboutus
# # Create your views here.

class AboutUsView(generic.ListView):
	template_name = "aboutus/aboutus.html"
	queryset = models.ChairPersonsRemarks.objects.all()

	def get_context_data(self, **kwargs):
		context = super(AboutUsView, self).get_context_data( **kwargs)
		context['chairpersonsremarks'] = models.ChairPersonsRemarks.objects.all()
		context['whoweare'] = models.WhoWeAre.objects.all()
		context['ourvision'] = models.OurVision.objects.all()
		context['ourmainobjective'] = models.OurMainObjective.objects.all()
		context['ourteam'] = models.OurTeam.objects.all()
		context['careers'] = models.Careers.objects.all()
		return context

class ContactUsCreateView(generic.CreateView):
    form_class = ContactUsForm
    template_name = "aboutus/contactus.html"

    success_url = reverse_lazy("aboutus:contact")
