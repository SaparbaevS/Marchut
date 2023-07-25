from django.shortcuts import render

from music3.models import Pop


def start_page(request):
    return render(request, 'index.html')

def show_pop(request):
    context = {"pop": Pop.objects.all()}
    return render(request, "pop.html", context=context)
