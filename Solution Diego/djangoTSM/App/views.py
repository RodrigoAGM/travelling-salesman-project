from django.views.generic import TemplateView, CreateView
from App.forms import HomeForm
from django.shortcuts import render
from solutionD import completaDiccionarios

def home(request):
    return render(request, 'app/home.html')

def sol1(request):
    context = {}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = completaDiccionarios('prueba.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Diego Salas' Solution",  'heading1': 'First solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context)  

def sol2(request):
    context = {}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = completaDiccionarios('prueba.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Andres Lopez's Solution",  'heading1': 'Third solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context) 

def sol3(request):
    context = {}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = completaDiccionarios('prueba.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Second solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context)  

def sol4(request):
    context = {}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = completaDiccionarios('prueba.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Second solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context)  