from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class UserInfo(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	email    = models.CharField(max_length=50)