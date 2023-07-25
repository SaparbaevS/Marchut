"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import music1.views
import music2.views
import music3.views
from music1.views import show_jazz, start_page
from music2.views import show_rok, start_page
from music3.views import show_pop, start_page


urlpatterns = [
    path('', start_page),
    path('music/jazz/', music1.views.show_jazz),
    path("music/", include("music1.urls")),

    path('music/rok/', music2.views.show_rok),
    path('music/', include('music2.urls')),

    path('music/pop/', music3.views.show_pop),
    path('music/', include('music3.urls')),

    path('admin/', admin.site.urls),
]
