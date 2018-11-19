import csv
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        print(u, v, w)

    #encontramos los padres 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #Unimos los subconjuntos por rango
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        #agregamos el arbol con menor rango al que tiene mayor rango
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #Si los rangos son iguales agrega un arbol a otro e incrementale el rango en 1
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        
    def KrustalMST(self, dictionary):
        result = [] # aqui se guarda el arbol de expansion minima

        i = 0
        e = 0

        #ordenamos las aristas de menor a mayor
        #creamos una copia del grafo (inmutable data)
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        #creamos N subconjuntos con elementos unicos
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        #vamos a guardar en los resultados n-1 aristas
        while e < self.V - 1:
            #elegimos la arista menor e incrementamos el indice para la siguiente itericion
            u, v, w = self.graph[i]

            print(u, v, w)
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            #si al incluir la arista no se genera un ciclo, inclumos esta en el arreglo de resultado e incrementamos el indice en 1
            if x != y:
                e += 1
                result.append([dictionary[u]['name'], dictionary[v]['name'], w])
                self.union(parent, rank, x, y)

        return result

def readFile(filename):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')

        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[5]
                elem["xCord"] = float(row[15])
                elem["yCord"] = float(row[16])
                dictionary[idelem] = elem
                del elem
            idelem += 1
        
        g = Graph(idelem)
        print('nodos:', g.V)

    return dictionary, g

def readCE(filename):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')

        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["distrito"] = row[3]
                elem["xCord"] = float(row[5])
                elem["yCord"] = float(row[6])
                dictionary[idelem] = elem
                del elem
            idelem += 1

        g = Graph(idelem)
        print('nodos:', g.V)

    return dictionary, g

def calcularDistancia(longitud1, longitud2, latitud1, latitud2):
    return ((longitud1-longitud2)**2 + (latitud1-latitud2)**2)**(0.5)

def makingDictonaries1(filename):
    dictionary, graph = readCE(filename)
    distancia={}
    #100
    for i in dictionary:
        aux = {}
        for j in dictionary:
            aux[j] = calcularDistancia(float(dictionary[i]["xCord"]),float(dictionary[j]["xCord"]),float(dictionary[i]["yCord"]),float(dictionary[j]["yCord"]))
            graph.addEdge(i, j, aux[j])

    return graph.KrustalMST(dictionary)


def makingDictonaries2(filename):
    dictionary, graph = readFile(filename)
    distancia={}
    #100
    for i in dictionary:
        aux = {}
        for j in dictionary:
            aux[j] = calcularDistancia(float(dictionary[i]["xCord"]),float(dictionary[j]["xCord"]),float(dictionary[i]["yCord"]),float(dictionary[j]["yCord"]))
            graph.addEdge(i, j, aux[j])

    return graph.KrustalMST(dictionary)

# def KruskalPath(filename, start, goal):
#     dictionary, graph = readFile(filename)
    
#     return graph.path(dictionary, makingDictonaries2(filename), start, goal)

# KruskalPath('datita.csv', 0, 1)

def dijkstraMOD(filename, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = makingDictonaries(filename)
    infinity = 999999
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for key, value in makingDictonaries(filename)[minNode].items():
            if value + shortest_distance[minNode] < shortest_distance[key]:
                shortest_distance[key] = value + shortest_distance[minNode]
                predecessor[key] = minNode
        unseenNodes.pop(minNode)
        
    currentNode = goal 
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return "Path not reachable"

    if shortest_distance[goal] != infinity:
        return shortest_distance[goal], path

def dijkstraMOD2(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999999
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for key, value in graph[minNode].items():
            if value + shortest_distance[minNode] < shortest_distance[key]:
                shortest_distance[key] = value + shortest_distance[minNode]
                predecessor[key] = minNode
        unseenNodes.pop(minNode)
        
    currentNode = goal 
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return "Path not reachable"

    if shortest_distance[goal] != infinity:
        return shortest_distance[goal], path






