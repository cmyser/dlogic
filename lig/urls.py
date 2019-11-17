from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    path('register/', RegisterFormView.as_view() , name='register_url'),
    path('login/', LoginFormView.as_view() , name='login_url'),
    path('logout/', LogoutView.as_view() , name='logout_url')

]
