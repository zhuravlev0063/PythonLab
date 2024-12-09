from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from .forms import CaseForm

def home(request):
    cases = Case.objects.all()
    return render(request, 'court/home.html', {'cases': cases})

def case_add(request):
    form = CaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'court/case_form.html', {'form': form})

def case_edit(request, pk):
    case = get_object_or_404(Case, pk=pk)
    form = CaseForm(request.POST or None, instance=case)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'court/case_form.html', {'form': form})

def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'court/case_detail.html', {'case': case})
