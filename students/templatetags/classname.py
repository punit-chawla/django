from django import template
from django.shortcuts import render,get_object_or_404,render_to_response
from manage_classes.models import *
register = template.Library()
@register.filter(name='cut')
def cut(value):
    classs = get_object_or_404(Classes, id=value)
    return classs.class_name
