from django.urls import path
from music3.views import show_pop

urlpatterns = [
    path('pop/', show_pop),

]