from django.shortcuts import render, redirect
from .models import Student
from django.db.models import Count
from .forms import StudentForm

# Create your views here.

def home(request):
    return render(request, 'Hostel_app/index.html')

def page1(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hostel_app:page2')
    else:
        form = StudentForm()
    
    return render(request, 'Hostel_app/page1.html', {'form': form})

def page2(request):
    # Get all students grouped by hostel with count
    hostel_data = Student.objects.values('hostel').annotate(
        student_count=Count('id')
    ).order_by('hostel')
    
    # Get all students ordered by hostel
    students_by_hostel = Student.objects.all().order_by('hostel', 'name')
    
    context = {
        'hostel_data': hostel_data,
        'students_by_hostel': students_by_hostel,
    }
    return render(request, 'Hostel_app/page2.html', context)
