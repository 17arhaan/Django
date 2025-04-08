from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'roll_no', 'hostel', 'room_no', 'date_joined')
    search_fields = ('name', 'email', 'roll_no', 'hostel')
    list_filter = ('hostel', 'date_joined')
