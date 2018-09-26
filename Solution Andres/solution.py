import csv
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


def makingDictonarys(filename):
    dictionary = readFile(filename)
    enlaces = {}
    distancia={}
    
    for i in range(1,len(dictionary)+1):
        aux={}
        aux2={}
        contador=1
        for j in range(1,len(dictionary)+1):
            contador+=1
            aux[j] = calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))
            aux2[j]=dictionary[i]["id"]
        if contador == len(dictionary)+1:
            distancia[i]=aux
            enlaces[i]=aux2
            del aux
            del aux2
    print(enlaces)
    #return dijkstra(enlaces, distance,dictionary)

"""
def dijkstra(enlaces, distance,dictionary):
    
    origen={}
    origen[0]=dictionary[0]["name"]
    origen[1]=dictionary[0]["x"]
    origen[2]=dictionary[0]["y"]

    path=[]
    distancia=distance
    enlace=enlaces
    unSeenNodes=[]
""" 
    #print(enlace[enlace[0]])



makingDictonarys("datasetTest.csv")


