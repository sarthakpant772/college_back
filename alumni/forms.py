from django import forms

class alumni_forms(forms.Form):
    photo = forms.ImageField(label='photo')