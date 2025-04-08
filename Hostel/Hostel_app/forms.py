from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll_no', 'hostel', 'room_no']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'roll_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'hostel': forms.Select(attrs={'class': 'form-control'}),
            'room_no': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Additional fields with different input types
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Gender'
    )
    
    meal_plan = forms.MultipleChoiceField(
        choices=[
            ('breakfast', 'Breakfast'),
            ('lunch', 'Lunch'),
            ('dinner', 'Dinner')
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label='Meal Plan'
    )
    
    year_of_study = forms.ChoiceField(
        choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Year of Study'
    )
    
    terms_agreed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I agree to the terms and conditions',
        required=True
    ) 