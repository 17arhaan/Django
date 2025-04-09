from django.shortcuts import render,redirect
from .models import book_app
from .forms import bookForm

# Create your views here.
def index(request):
    return render(request,'book_app/index.html')

def page1(request):
    form = bookForm()
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_app:page2')
    return render(request, 'book_app/page1.html', {'form': form})

def page2(request):
    context = {
        'books' : book_app.objects.all(),
        'total_books' : book_app.objects.count(),
    }
    return render(request,'book_app/page2.html',context)