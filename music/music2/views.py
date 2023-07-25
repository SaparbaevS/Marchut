from django.shortcuts import render

from music2.models import Rok


def start_page(request):
    return render(request, 'index.html')

def show_rok(request):
    context = {"rok": Rok.objects.all()}
    return render(request, "rok.html", context=context)


