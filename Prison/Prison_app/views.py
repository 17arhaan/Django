from django.shortcuts import render, redirect
from .models import Prisoner
from .forms import PrisonerForm

# Create your views here.
def index(request):
    return render(request, 'Prison_app/index.html')

def page1(request):
    form = PrisonerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Prison_app:page2')
    return render(request, 'Prison_app/page1.html', {'form': form})

def page2(request):
    context = {
        'prisoners': Prisoner.objects.all(),
        'total_prisoners': Prisoner.objects.count(),
    }
    return render(request, 'Prison_app/page2.html', context)


