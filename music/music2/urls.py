from django.contrib import admin
from django.urls import path
from music2.views import show_rok

urlpatterns = [
    path('rok/', show_rok),

]