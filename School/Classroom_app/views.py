from django.shortcuts import render, redirect
from .models import Classroom_app
from .forms import ClassroomForm

# Create your views here.

def index(request):
    return render(request, 'Classroom_app/index.html')

def page1(request):
    form = ClassroomForm()  # Create form instance
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('Classroom_app:page2')
    return render(request, 'Classroom_app/page1.html', {'form': form})  # Pass form to template

def page2(request):
    context = {
    'students' : Classroom_app.objects.all(),
    'total_students' : Classroom_app.objects.count(),
    }
    return render(request, 'Classroom_app/page2.html', context)