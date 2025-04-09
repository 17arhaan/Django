from django.shortcuts import render, redirect
from .models import Classroom_app
from .forms import ClassroomForm
from django.db.models import Count

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
    # Order students by name
    students_ordered = Classroom_app.objects.all().order_by('name')

    # Count total students
    total_students = Classroom_app.objects.count()

    # Group by class and count students in each class
    students_by_class = Classroom_app.objects.values('class_name').annotate(total=Count('id'))

    # Example: Handling dropdown choices
    # Assume there's a model for choices and user selections
    selected_choices = UserSelection.objects.filter(user=request.user).values_list('choice', flat=True)
    available_choices = Choice.objects.exclude(id__in=selected_choices)

    context = {
        'students_ordered': students_ordered,
        'total_students': total_students,
        'students_by_class': students_by_class,
        'available_choices': available_choices,
    }

    return render(request, 'Classroom_app/page2.html', context)