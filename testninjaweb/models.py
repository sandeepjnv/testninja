from django.db import models

# Create your models here.
class Workflow(models.Model):
    name = models.CharField(max_length=15)
    suiteName = models.CharField(max_length=50)
    workflowconfig = models.JSONField()