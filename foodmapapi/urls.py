"""foodmapapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

import api.urls
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.views.marker_list),
    path('search/<str:score>', api.views.search_place),
    path('place_detail/<int:place_id>', api.views.update_place_contents),
    path('api/', include(api.urls.urlpatterns)),
]

urlpatterns += staticfiles_urlpatterns()
