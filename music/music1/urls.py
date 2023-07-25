from django.contrib import admin
from django.urls import path
from music1.views import show_jazz

urlpatterns = [
    path('jazz/', show_jazz),


]