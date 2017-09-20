from __future__ import absolute_import

from django.views import generic

from .models import Members

class MembersListView(generic.ListView):
	model = Members
	template_name  = "members/member_list.html"
