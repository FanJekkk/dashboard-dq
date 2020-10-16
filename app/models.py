# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class subscriber(models.Model):
    name = models.CharField(max_length=55)
    err = models.IntegerField()

    class Meta:
        db_table = "subscribers"

    def __str__(self):
        return self.name
