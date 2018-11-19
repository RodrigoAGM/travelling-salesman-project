from django.views.generic import TemplateView, CreateView
from App.forms import HomeForm
from django.shortcuts import render
from solutionD2 import dijkstraMOD, dijkstraMOD2, makingDictonaries2, makingDictonaries1 #diego
from solutionA1 import dij #andres
from shortest_route3 import readCSV, readCSVIE, TSP #Roddrigo
from tf import makingDictonarys #andres


def home(request):
    return render(request, 'app/home.html')

def sol1(request):
    context = {'title': "Diego Salas' Solution",  'heading1': 'First solution', 'active': False}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = dijkstraMOD('datita.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Diego Salas' Solution",  'heading1': 'First solution',
        'shortestPath': shortestPath, 'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context)  

def sol2(request):
    context = {'title': "Andres Lopez's Solution",  'heading1': 'Second solution', 'active': False}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        path = dij('datita.csv', start)
        context = {'start': start, 'title': "Andres Lopez's Solution",  'heading1': 'Second solution',
        'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context) 

def sol3(request):
    context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Third solution', 'active': False}

    if request.method == "POST":
        populated_centers = readCSV('testdataset.csv')
        path = TSP(populated_centers)
        context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Third solution',
        'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context)  

def sol4(request):
    context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Fourth solution', 'active': False}

    if request.method == "POST":
        context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Fourth solution',
        'active': True }
        
    return render(request, 'app/solutions.html', context)  

def sol5(request):
    context = {'title': "Andres Lopez's Solution",  'heading1': 'Fifth solution: prim', 'active': False}

    if request.method == "POST":
        path = makingDictonarys("datasetA.csv")
        context = {'title': "Andres Lopez's Solution",  'heading1': 'Fifth solution: prim',
        'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context)  

def sol6(request):
    context = {'title': "Diego Salas' Solution Kruskal",  'heading1': 'Sixth solution: centros poblados', 'active': False}

    if request.method == "POST":
        path = makingDictonaries2('1000.csv')
        print(path)
        context = {'title': "Diego Salas' Solution Kruskal",  'heading1': 'Sixth solution: centros poblados',
        'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context)  

def sol7(request):
    context = {'title': "Diego Salas' Solution Kruskal",  'heading1': 'seventh solution: centros educativos', 'active': False}

    if request.method == "POST":
        path = makingDictonaries1('testCE.csv')
        print(path)
        context = {'title': "Diego Salas' Solution Kruskal",  'heading1': 'seventh solution: centros educativos',
        'path': path, 'active': True}
        
    return render(request, 'app/solutions.html', context)  

    