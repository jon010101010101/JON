from django import forms

class LogForm(forms.Form):
    text = forms.CharField(max_length=255)
