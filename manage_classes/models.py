from __future__ import unicode_literals
import  datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Classes(models.Model):
    class_name = models.CharField(max_length = 200)
    add_date = models.DateTimeField('date added')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.class_name




class Sections(models.Model):
    classs = models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_name = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')

    def __str__(self):
        return self.section_name
