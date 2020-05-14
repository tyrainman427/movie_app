from django.shortcuts import render
from .models import Film
from .forms import SearchForm
from .apis import search_film, get_film
import json
import requests


def button(request):
    django_list = []
    print("Hitting button function")
    
    with open('film_data.json', 'r') as content:
        data = json.load(content)
        for item in data['titles']:
            django_list.append(item['id'])

    return render(request,'film/search_film.html',{})

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


