from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=False)
    author = forms.CharField(label='Author', max_length=100, required=False)
    publication_year = forms.IntegerField(label='Publication Year', required=False)
    category = forms.CharField(label='category', max_length=100, required=False)
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'category']


 
