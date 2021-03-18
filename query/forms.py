from django import forms

class JoinForm(forms.Form): # or forms.ModelForm
    query = forms.CharField(max_length=120)