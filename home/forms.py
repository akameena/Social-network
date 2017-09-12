from django import forms
from home.models import post

class HomeForm(forms.ModelForm):
    post = forms .CharField(widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Write a post...'
            
        }
    ))

    class Meta:
        model = post
        fields = ('post',)