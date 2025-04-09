from django import forms
from .models import book_app

class bookForm(forms.ModelForm):
    class Meta:
        model = book_app
        fields = ['book_name','book_genre']
        