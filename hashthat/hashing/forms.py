from django import forms

class HashForm(forms.Form):

    text = forms.CharField(label = 'Enter Hash Here', widget = forms.Textarea )