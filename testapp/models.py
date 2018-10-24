from django.db import models

class EventData(models.Model):
	name = models.CharField(max_length=100,null=False)
	date = models.DateField(null = False)
	description = models.CharField(max_length=750,null=False)
	event_id = models.AutoField(primary_key=True)
	city = models.CharField(max_length=30)