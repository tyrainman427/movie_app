from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Film
from .forms import SearchForm
from .apis import search_film
import requests




class SearchPageView(TemplateView):
    template_name = 'film/search_film.html'

# def view_name(request):
#
#     if request.method == "POST":
#         movie = request.POST.get("handle", None)  # handle is the name of the input in the question.
#     # Here you can do anything with your screenname, like passing it to the function.
#         print(movie)
#     return render(request, 'film/search_film.html', {})

class FilmPage(TemplateView):
    def get(self,request):
        title_list = search_film()
        return render(request,'film/search_film.html',title_list)

def view_name(request):

    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            title2 = form.search()
            print("title2: ",title2)
            # form.save()
            # search_film(title)
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = SearchForm() # An unbound form

    return render(request,'film/search_film.html',{'form':form})
