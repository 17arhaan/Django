from django.shortcuts import render
from .models import Student
from django.db.models import Count

# Create your views here.

def home(request):
    return render(request, 'Hostel_app/index.html')

def page1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_no = request.POST.get('rollno')
        hostel = request.POST.get('hostel')
        room_no = request.POST.get('roomno')
        
        Student.objects.create(
            name=name,
            email=email,
            roll_no=roll_no,
            hostel=hostel,
            room_no=room_no
        )
    
    return render(request, 'Hostel_app/page1.html')

def page2(request):
    # Get all students grouped by hostel with count
    hostel_data = Student.objects.values('hostel').annotate(
        student_count=Count('id')
    ).order_by('hostel')
    
    # Get all students for each hostel
    students_by_hostel = {}
    for hostel in hostel_data:
        students = Student.objects.filter(hostel=hostel['hostel']).order_by('name')
        students_by_hostel[hostel['hostel']] = students
    
    context = {
        'hostel_data': hostel_data,
        'students_by_hostel': students_by_hostel,
    }
    return render(request, 'Hostel_app/page2.html', context)
