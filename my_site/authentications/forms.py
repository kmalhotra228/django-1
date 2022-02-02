from django import forms
from .models import Joinee,Personal_details
from django.forms import ModelForm

class ReviewForm(ModelForm):

    class Meta:
        model = Personal_details
        fields = ('username','first_name','last_name','email','phone_number','date_of_birth','gender')
        widgets = {
                    'date_of_birth': forms.DateInput(attrs={'type':'date'})


        }

        
