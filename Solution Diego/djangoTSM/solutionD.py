import csv

def calcularDistancia(longitud1, longitud2, latitud1, latitud2):
    return ((longitud1-longitud2)**2 + (latitud1-latitud2)**2)**(0.5)

def dijkstra(dicEnlaces, dicPesos, start, goal):
    
    shortest_distance = {}
    predecessor = {}
    unseenNodes = dicEnlaces
    distanciaNodos = dicPesos
    infinity = 999999
    path = []
    
    for node in distanciaNodos:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        
        if distanciaNodos[minNode] + shortest_distance[minNode] < shortest_distance[unseenNodes[minNode]]:
            shortest_distance[unseenNodes[minNode]] = distanciaNodos[minNode] + shortest_distance[minNode] 
            predecessor[unseenNodes[minNode]] = minNode
        unseenNodes.pop(minNode)
    
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            return 'No existe camino', None

    if shortest_distance[goal] != infinity:
        return shortest_distance[goal], path
    

def readCSV(filename):
    """
    Function that recieves a filename, reads that csv file and returns a dictionary with 
    the name, xcord and ycord of each populated center of the file. 
    """
    dictionary = {}
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = 1
        for row in file:
            elem = {}
            elem["id"] = row[0]
            elem["nombre"] = str(row[1])
            elem["idForaneo"] = int(row[2])
            elem["longitud"] = float(row[3])
            elem["latitud"] = float(row[4])
            dictionary[idelem] = elem
            del elem   
            idelem += 1

    return dictionary

def completaDiccionarios(filename, start, goal):
    
    dictionary = readCSV(filename)
    dicPesos = {}
    dicEnlaces = {}
    dicAsignacionID = {}

    for key in dictionary:
        dicPesos[key] = calcularDistancia(dictionary[key]['longitud'],dictionary[dictionary[key]['idForaneo']]['longitud'],
                                         dictionary[key]['latitud'], dictionary[dictionary[key]['idForaneo']]['latitud'])
        dicEnlaces[key] = dictionary[key]['idForaneo']
        dicAsignacionID[key] = dictionary[key]['nombre']

    return dijkstra(dicEnlaces, dicPesos, start, goal)