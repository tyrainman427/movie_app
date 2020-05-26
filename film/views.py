from django.shortcuts import render
from .models import Film
from .forms import SearchForm
import requests
from django.views.generic import View
from film import apis
import json



def view_name(request):


    apis.get_film()
    data = apis.film_list

    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            # form.save()
            context = {
            
            }
            print("Searching for films....")
            return render(request,'film/search_film.html',context)

    else:
        form = SearchForm() # An unbound form

    return render(request,'film/search_film.html',{'form':form})


def get_detail(request):

    return render(request, 'film/search_results.html',{})
