import csv
def readFile(filename):
    dictionary = {}
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["x"] = float(row[2])
                elem["y"] = float(row[3])
                dictionary[idelem] = elem
                del elem
                
            idelem += 1
    #print(dictionary[0]["name"]) -> Huamampallpa
    return dictionary

def calculateDistance(x1,y1,x2,y2):        
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

def dijkstra(enlaces, distance):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = enlaces
    distanciaNodos = distance
    infinity=99999
    
    for node in distanciaNodos:
        shortest_distance[node] = infinity
    shortest_distance[0]=0


    """
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node 
            elif shortest_distance[node] > shortest_distance[minNode]:
                minNode = node
        
        if distanciaNodos[minNode] + shortest_distance[minNode] < shortest_distance[unseenNodes[minNode]]:
            shortest_distance[unseenNodes[minNode]] = distanciaNodos[minNode] + shortest_distance[minNode] 
            predecessor[unseenNodes[minNode]] = minNode
        unseenNodes.pop(minNode)
        """
    dist=0
    for i in range(len(shortest_distance)):
        if dist>shortest_distance[i]:
           dist>shortest_distance[i] 

    return dist
    

def makingDictonarys(filename):
    
    dictionary = readFile(filename)
    distance = {}
    nodo={}
    keyFor={}
    enlaces = {}

    for i in range(len(dictionary)):
        for j in range(1,len(dictionary)):
            nodo = calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))
            keyFor=dictionary[i]["id"]
            distance[i]=nodo
            enlaces[i] = keyFor
            del nodo
            del keyFor
        
    dijkstra(enlaces, distance)

print(makingDictonarys("datasetTest.csv"))