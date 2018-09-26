from django.shortcuts import render
from django.http import HttpResponse
from solutionD import completaDiccionarios

# Home

def home(request):
    return render(request, 'app/home.html')

# first solution 

start, goal = 1, 2
path = []
shortestPath, path = completaDiccionarios('prueba.csv', start, goal)

def sol1(request):
    context = {
        'title': "Diego Salas' Solution",
        'heading1': 'First solution',
        'start': start,
        'goal': goal,
        'shortestPath': shortestPath,
        'path': path
    }
    return render(request, 'app/solutions.html', context)

# second solution 

start2, goal2 = 1, 5
path2 = []
shortestPath2, path2 = completaDiccionarios('prueba.csv', start2, goal2)

def sol2(request):
    context = {
        'title': "Rodrigo Guadalupe's Solution",
        'heading1': 'Second solution',
        'start': start2,
        'goal': goal2,
        'shortestPath': shortestPath2,
        'path': path2
    }
    return render(request, 'app/solutions.html', context)

# third solution 

start3, goal3 = 5, 2
path3 = []
shortestPath3, path3 = completaDiccionarios('prueba.csv', start3, goal3)

def sol3(request):
    context = {
        'title': "Andres Lopez's Solution",
        'heading1': 'Third solution',
        'start': start3,
        'goal': goal3,
        'shortestPath': shortestPath3,
        'path': path3
    }
    return render(request, 'app/solutions.html', context)