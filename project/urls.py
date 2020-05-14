from django.urls import path, include
from django.contrib import admin
from film.views import button



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film.urls'))
]
