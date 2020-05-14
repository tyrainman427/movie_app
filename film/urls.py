from django.urls import path

from .views import view_name, button

app_name = 'movie'

urlpatterns = [
    path('', view_name, name='search_results'),
    path('', button),
    # path('details/', film_details, name='details'),
]
