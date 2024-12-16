# court_case/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from .forms import CaseForm

def index(request):
    cases = Case.objects.all()
    return render(request, 'court_case/index.html', {'cases': cases})

def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'court_case/case_detail.html', {'case': case})

def add_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CaseForm()
    return render(request, 'court_case/add_case.html', {'form': form})