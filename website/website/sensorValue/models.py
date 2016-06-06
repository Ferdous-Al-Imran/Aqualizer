from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	# userId=models.AutoField(primary_key=True,editable=False)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=30)
	firstName=models.CharField(max_length=50)
	lastName=models.CharField(max_length=50)
	email=models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('sensorValue:sensorValue',kwargs={'pk':self.pk})

	def __str__(self):
		return self.username + ' - ' + self.email
	


class ParameterList(models.Model):
	parameterId=models.AutoField(primary_key=True)
	parameterName=models.CharField(max_length=50)

	def __str__(self):
		return str(self.parameterId) + ' - ' + str(self.parameterName
		)
class ValueEntry(models.Model):
	valueTime=models.DateTimeField(auto_now_add=True, blank=True,primary_key=True)
	userId=models.ForeignKey(User, on_delete=models.CASCADE)
	parameterId=models.ForeignKey(ParameterList, on_delete=models.CASCADE)
	parameterValue=models.FloatField()


	def __str__(self):
		return str(self.userId) + ' - ' + str(self.valueTime) + ' - ' + str(self.parameterValue)


class ParameterIdeals(models.Model):
	userId=models.ForeignKey(User, on_delete=models.CASCADE)
	parameterId=models.ForeignKey(ParameterList, on_delete=models.CASCADE)
	standardValue=models.FloatField()
	safeUpperValue=models.FloatField()
	safeLowerValue=models.FloatField()



	def __str__(self):
		return str(self.userId) + ' - ' + str(self.parameterId) + ' - ' + str(self.standardValue)