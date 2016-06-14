from __future__ import unicode_literals

from django.db import models

# Create your models here.

class posts(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharFiels(max_length=100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

