from django.http import HttpResponse
from django.shortcuts import render

from music1.models import Jazz
from music2.models import Rok


def start_page(request):
    return render(request, 'index.html')

def show_jazz(request):
    context = {"jazz": Jazz.objects.all()}
    return render(request, "jazz.html", context=context)



