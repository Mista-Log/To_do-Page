from django import forms
from .models import List


class ListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'btn:hover', 'placeholder': 'Enter to_do'}))
    class Meta:
        model = List
        fields = ["title"]