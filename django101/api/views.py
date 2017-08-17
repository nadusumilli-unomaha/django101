# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import generic

from django.contrib.auth.models import *

class IndexView(generic.ListView):
    """Show a list of all experiments"""
    model = User
    template_name = 'api/index.html'
    context_object_name = 'current_experiments'

class RegisterView(generic.ListView):
	# Please complete this view and html file.
	model = User

	

