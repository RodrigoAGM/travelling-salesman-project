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
    return dictionary

def calculateDistance(x1,y1,x2,y2):        
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)


def makingDictonarys(filename):
    dictionary = readFile(filename)
    aux={}
    aux2={}
    distance = {}
    distancia={}
    keys={}
    enlaces = {}
    
    for i in range(len(dictionary)):
        contador=0
        for j in range(1,len(dictionary)):
            distancia = calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))
            keys=dictionary[i]["id"]
            contador+=1
            aux[j]=distancia          
            aux2[j] = keys
            del keys
            del distancia
        if contador ==10:
            distance[j]= aux
            enlaces[j]=aux2
    del aux
    del aux2
    return dijkstra(enlaces, distance,dictionary)



def dijkstra(enlaces, distance,dictionary):
    
    origen={}
    origen[0]=dictionary[0]["name"]
    origen[1]=dictionary[0]["x"]
    origen[2]=dictionary[0]["y"]

    path=[]
    distancia=distance
    enlace=enlaces
    """
    for i in range(len(dictionary)):
        for j in range(1,len(dictionary)):
            if enlace[i] < enlace[j]:
                menor=enlace[i]"""

    print(enlace[enlace[0]])



makingDictonarys("datasetTest.csv")


