from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    path('', get_name , name='coment_url'),

]
