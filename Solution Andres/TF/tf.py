import csv
import math
import heapq as hq
def readFile(filename):
    dictionary = {}
    with open(filename,encoding='utf-8-sig') as csvfile:
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
    distancia=[]
    nombre=[]
    for i in range(1,len(dictionary)+1):
        aux=[]
        aux2=[]
        for j in range(1,len(dictionary)+1):
            aux.append((int(dictionary[j]["id"]),calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))))
            aux2.append(dictionary[j]["name"])
            #aux.append((j,calculateDistance(float(dictionary[i]["x"]),float(dictionary[i]["y"]), float(dictionary[j]["x"]),float(dictionary[j]["y"]))))
        distancia.append(aux)
        nombre.append(aux2)
        del aux
        del aux2
    #print(nombre)
    prim(distancia,nombre)

def prim(distancia,nombre):
    n = len(distancia)
    dist = [math.inf]*n
    path = [None]*n
    visited = [False]*n
    q = []
    hq.heappush(q, (0, 0))
    contador=0
    while len(q) > 0:
        print(contador)
        contador+=1
        _, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in distancia[u]:
                if not visited[v] and w < dist[v] and w!=0 :
                    dist[v] = w
                    path[v] = nombre[v][u]
                    hq.heappush(q, (w, v))
    print(path)


makingDictonarys("dataset.csv")