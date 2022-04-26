# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unicodedata import name

from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)