from django.db import models
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *


# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# class Person(User):
#     us = User.


class Name(models.Model):
    name = models.CharField(max_length=100)
