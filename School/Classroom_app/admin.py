from django.contrib import admin
from .models import Classroom_app
from .forms import ClassroomForm
# Register your models here.

@admin.register(Classroom_app)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_grade','student_section','total_marks','student_disablity','teacher_name','admission_date')
    search_fields = ('student_name','teacher_name')
    list_filter = ('teacher_name',)