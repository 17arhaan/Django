from django import forms
from .models import Prisoner

class PrisonerForm(forms.ModelForm):
    class Meta:
        model = Prisoner
        fields =['prisoner_id','name','age','block_number','cell_number','admission_date','release_date','crime']
        widgets = {
            'admission_date':forms.DateInput(attrs={'type':'date'}),
            'release_date':forms.DateInput(attrs={'type':'date'}),
        }