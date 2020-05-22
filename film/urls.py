from django.urls import path
from .views import view_name, get_detail

app_name = 'movie'

urlpatterns = [
    path('', view_name, name='search_results'),
    path('details/', get_detail, name='movie_details'),
    # path('details/', film_details, name='details'),
]
