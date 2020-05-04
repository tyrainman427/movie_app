from django.shortcuts import render
from .models import Film
from .forms import SearchForm
from .apis import search_film, get_film
import requests


def view_name(request):

    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            # form.save()
            context = {
                "films":search_film(title)
            }
            print("Searching for films....")
            return render(request,'film/search_film.html',context)

    else:
        form = SearchForm() # An unbound form

    return render(request,'film/search_film.html',{'form':form})


def film_details(request):
    context = {
        "flix":get_film()
    }
    print("Pulling the film details....")
    return render(request,'film/search_results.html',context)
