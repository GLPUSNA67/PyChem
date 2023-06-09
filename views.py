from django.shortcuts import render

# Create your views here.

def landingpage(request):
    return render(request, 'matrix/index.html', {})

def uielements(request):
    return render(request, 'matrix/ui-elements.html', {})

def lpchart(request):
    return render(request, 'matrix/chart.html', {})

def lptabpanel(request):
    return render(request, 'matrix/tab-panel.html', {})

def lptable(request):
    return render(request, 'matrix/table.html', {})

def lpform(request):
    return render(request, 'matrix/form.html', {})

def lpempty(request):
    return render(request, 'matrix/empty.html', {})
