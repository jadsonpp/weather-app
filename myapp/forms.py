from django import forms


    
class CityForm(forms.Form):
    name = forms.CharField(label='city',max_length=100)


