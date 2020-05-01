from django import forms
from .models import Film

class SearchForm(forms.ModelForm):
    title = forms.CharField(label='Movie', max_length=300)

    class Meta:
        model = Film
        fields = ['title']
