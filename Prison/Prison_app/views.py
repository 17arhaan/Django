from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Prisoner
from .forms import PrisonerForm

# Create your views here.
def index(request):
    return render(request, 'Prison_app/index.html')

def page1(request):
    if request.method == 'POST':
        form = PrisonerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Prison_app:page2')
    else:
        form = PrisonerForm()
    return render(request, 'Prison_app/page1.html', {'form': form})

def page2(request):
    prisoners = Prisoner.objects.all().order_by('block_number', 'cell_number')
    prisoner_count = prisoners.count()
    prisoners_by_block = Prisoner.objects.values('block_number').annotate(
        count=Count('id')
    ).order_by('block_number')
    
    context = {
        'prisoners': prisoners,
        'total_prisoners': prisoner_count,
        'prisoners_by_block': prisoners_by_block,
    }
    return render(request, 'Prison_app/page2.html', context)


