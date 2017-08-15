# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User, Group

# Create your models here.
class Profile(models.Model):
	role = models.CharField(max_length=100)
	# This class should have the following attributes
	# Age, int, max length 3, required
	# City, string, required
	# State, string, required
	# gender, restrict choices to male or female, requried
	# education string nullable
	# User one to one relationship to the user model and on delete cascade.