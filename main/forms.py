from django.forms import forms
from django import forms


class AddItemForm(forms.Form):

    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()


