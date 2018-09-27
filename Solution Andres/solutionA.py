import csv
import copy

path = []
infinity = 999999

def readFile(filename):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        contador=1
        for row in file:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["x"] = float(row[2])
                elem["y"] = float(row[3])
                dictionary[contador] = elem
                contador+=1
                del elem

    return dictionary

def calculateDistance(x1,y1,x2,y2):        
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)


def makingDictonarys(filename, start):
    dictionary = readFile(filename)
    enlaces = {}
    distancia={}
    
    for i in range(1,len(dictionary)+1):
        aux=[]
        aux2=[]
        contador=1
        for j in range(1,len(dictionary)+1):
            contador+=1
            aux.append(calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"])))
            aux2.append(dictionary[i]["id"])
        if contador == len(dictionary)+1:
            distancia[i]=aux
            enlaces[i]=aux2
            del aux
            del aux2
    
    dijkstraMOD(enlaces, distancia, dictionary, start)

def dijkstraMOD(enlaces, distancia, dictionary, start):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = enlaces
    nodes = distancia
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0.0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        
        for key, value in nodes.items():
            if shortest_distance[minNode] + value[minNode-1] < shortest_distance[key]:
                shortest_distance[key] = shortest_distance[minNode] + value[minNode-1] 
                predecessor[key] = minNode
        break

    for i in nodes:
        if len(nodes[i])==start:
            continue    
        nodes[i].pop(start-1)  

    shortest_distance.pop(start)
    nodomenor = infinity

    for i in unseenNodes:
        if len(unseenNodes[i])==start:
            continue    
        unseenNodes[i].pop(start-1)
    
    contador=0
    for k,v in shortest_distance.items():
        if nodomenor > v and nodomenor !=0:
            contador+=1
            nodomenor=v

    start = contador
    for i in shortest_distance:
        if i == contador:
            path.append(dictionary[i]["name"])
    
    for i in predecessor:
        predecessor[i] = start


    print(path)

    dijkstraMOD(unseenNodes, nodes, dictionary, start)

makingDictonarys("datasetTest.csv", 3)


