from __future__ import unicode_literals
from django.contrib.auth.models import User
import  datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200)
    classs = models.IntegerField(max_length=11)
    add_date = models.DateTimeField('date added')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
