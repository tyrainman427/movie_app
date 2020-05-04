from django.urls import path

from .views import view_name, film_details

app_name = 'movie'

urlpatterns = [
    path('', view_name, name='search_results'),
    path('details/', film_details, name='details'),
]
