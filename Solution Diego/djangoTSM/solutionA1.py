import csv
def readFile(filename):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["xCord"] = float(row[15])
                elem["yCord"] = float(row[16])
                dictionary[idelem] = elem
                del elem
            idelem += 1
    return dictionary

def calcularDistancia(longitud1, longitud2, latitud1, latitud2):
    return ((longitud1-longitud2)**2 + (latitud1-latitud2)**2)**(0.5)


def makingDictonaries(filename):
    dictionary = readFile(filename)
    distancia={}
    #1000
    for i in dictionary:
        aux = {}
        for j in dictionary:
            aux[j] = calcularDistancia(float(dictionary[i]["xCord"]),float(dictionary[j]["xCord"]),float(dictionary[i]["yCord"]),float(dictionary[j]["yCord"]))
        distancia[i] = aux

    return distancia

def dij(filename, start):
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
    
    return shortest_distance





