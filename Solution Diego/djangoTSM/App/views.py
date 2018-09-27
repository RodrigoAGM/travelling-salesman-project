from django.views.generic import TemplateView, CreateView
from App.forms import HomeForm
from django.shortcuts import render
from solutionD2 import dijkstraMOD, dijkstraMOD2 #diego
from solutionA1 import dij #andres
from shortest_route import TSP #rodrigo
from shortest_route2 import CalculatePahts #rodrigo
from basic_functions import readCSV1, calculateDistances #rodrigo
from basic_functions2 import readCSV, calculateDistancesDictionary #rodrigo

def home(request):
    return render(request, 'app/home.html')

def sol1(request):
    context = {'title': "Diego Salas' Solution",  'heading1': 'First solution'}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        goal =  int(request.POST.get("goal"))
        shortestPath, path = dijkstraMOD('datita.csv', start, goal)
        context = {'start': start, 'goal': goal, 'title': "Diego Salas' Solution",  'heading1': 'First solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context)  

def sol2(request):
    context = {'title': "Andres Lopez's Solution",  'heading1': 'Second solution'}

    if request.method == "POST":
        start =  int(request.POST.get("start"))
        path = dij('datita.csv', start)
        context = {'start': start, 'title': "Andres Lopez's Solution",  'heading1': 'Second solution',
        'path': path}
        
    return render(request, 'app/solutions.html', context) 

def sol3(request):
    context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Third solution'}

    if request.method == "POST":
        populated_centers = readCSV1('testdataset.csv')
        distance_matrix = calculateDistances(populated_centers)
        path = TSP(distance_matrix, populated_centers, 0)
        context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Third solution',
        'path': path}
        
    return render(request, 'app/solutions.html', context)  

def sol4(request):
    context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Fourth solution'}

    if request.method == "POST":
        palcesDictionary, places = readCSV('testdataset.csv')
        distancesDictionary = calculateDistancesDictionary(palcesDictionary, places)
        path = CalculatePahts(distancesDictionary, places, palcesDictionary)
        context = {'title': "Rodrigo Guadalupe's Solution",  'heading1': 'Fourth solution',
        'path': path }
        
    return render(request, 'app/solutions.html', context)  

def sol5(request):
    context = {'title': "Diego Salas' Solution esp",  'heading1': 'Fifth solution'}
    graph = {'a': {'b':10,'c':3 },'b': {'c':1,'d':2},'c': {'b':4,'d':8,'e':2},'d': {'e':7},'e': {'d':9}} 

    if request.method == "POST":
        start = request.POST.get("start")
        goal = request.POST.get("goal")
        shortestPath, path = dijkstraMOD2(graph, start, goal)
        context = {'start': start, 'goal': goal, 'title': "Diego Salas' Solution esp",  'heading1': 'Fifth solution',
        'shortestPath': shortestPath, 'path': path}
        
    return render(request, 'app/solutions.html', context)  

    