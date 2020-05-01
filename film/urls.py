from django.urls import path

from .views import SearchPageView, view_name, FilmPage

urlpatterns = [
    path('', view_name, name='search_results'),
    # path('', SearchPageView.as_view(), name='home'),
]
