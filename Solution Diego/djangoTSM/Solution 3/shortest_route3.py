import csv
import math

def readCSV(filename):
    """
    Function that recieves a filename, reads that csv file and returns an array
    of dictionaries with the name, xcord and ycord of each populated center of the file. 
    """
    array = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["xCord"] = float(row[15])
                elem["yCord"] = float(row[16])
                array.append(elem)
                del elem
            
            idelem += 1
    
    return array

def readCSVIE(filename):
    """
    Function that recieves a filename, reads that csv file and returns an array
    of dictionaries with the name, xcord and ycord of each populated center of the file. 
    """
    array = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[1]
                elem["xCord"] = float(row[5])
                elem["yCord"] = float(row[6])
                array.append(elem)
                del elem
            
            idelem += 1
    
    return array

def getShortestNode(distances):
    """
    Function that finds the position of the shortest element of an array
    """
    n = len(distances)
    if n == 0:
        return -1

    def min(array, i, j):
        if i == j:
            return i
        else:
            med = int((i+j) / 2)
            medIzq = min(array,i,med)
            medDer = min(array,med+1,j)
            if array[medDer] == 0:
                return medIzq
            elif array[medIzq] == 0:
                return medDer
            elif array[medDer] < array[medIzq]:
                return medDer
            else:
                return medIzq

    return min(distances,0,n-1)

def TSP(populated_centers):
    """
    Function that recieves an array of dictionaries and generates a distance matrix for all
    the possible connections between two pairs of populated centers and returns the path of
    the best route.
    """
    path = []
    row = []
    n = len(populated_centers)
    visited = [False] * n
    fil = 0

    while len(path) != n:
        for col in range(n):

            if not visited[col]:
                if fil == col:
                    row.append(0)
                else:
                    operation = ((populated_centers[col]["xCord"]) - (populated_centers[fil]["xCord"]))**2 + ((populated_centers[col]["yCord"] - populated_centers[fil]["yCord"]))**2
                    distance = operation**0.5
                    row.append(distance)
            else:
                row.append(math.inf)

        path.append(populated_centers[fil]["name"])
        pos = getShortestNode(row)
        visited[fil] = True
        fil = pos
        row.clear()

    return path
