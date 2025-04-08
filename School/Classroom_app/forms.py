from django import forms
from .models import Classroom_app

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom_app
        fields = ['student_name','student_grade','student_section','total_marks','student_disablity','teacher_name','admission_date']
        widgets = {
            'admission_date':forms.DateInput(attrs = {'type':'date'}),
        }
