from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=30)
	firstName=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
