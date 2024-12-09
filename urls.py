from django.contrib import admin
from django.urls import path, include
from cases import urlpatterns as cases_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cases_urls)),
]
