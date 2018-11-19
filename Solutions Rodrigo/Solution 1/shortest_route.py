from basic_functions import *

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

def rebuildArrays(distance_matrix, populated_centers, delPos):
    """
    Function that returns two rebuilded arrays without the delPos position
    """
    n = len(distance_matrix)        

    for pos in range(n):
        if delPos == n-1:
            distance_matrix[pos] = distance_matrix[pos][0:delPos]
        else: 
            if delPos == 0:
                distance_matrix[pos] = distance_matrix[pos][1:]
            else:
                distance_matrix[pos] = distance_matrix[pos][0:delPos] + distance_matrix[pos][delPos+1:]
                
    if delPos == 0:
        distance_matrix = distance_matrix[1:]
        populated_centers = populated_centers[1:]
    else:
        if delPos == n-1:
            distance_matrix = distance_matrix[0:delPos]
            populated_centers = populated_centers[0:delPos]
        else:
            distance_matrix = distance_matrix[0:delPos] + distance_matrix[delPos+1:]
            populated_centers = populated_centers[0:delPos] + populated_centers[delPos+1:]
    
    return distance_matrix, populated_centers

def TSP(distance_matrix, populated_centers, pos):
    """
    Function that returns the path of the shortest route to visit every
    populated center of the dataset.
    """
    n = len(distance_matrix)
    path = []

    while len(path) != n:
        newpos = getShortestNode(distance_matrix[pos])
        path.append(populated_centers[pos]["name"])
        distance_matrix, populated_centers = rebuildArrays(distance_matrix, populated_centers,pos)
        if newpos < pos:
            pos = newpos
        else:
            pos = newpos-1

    print(path)

populated_centers = readCSV('testdataset.csv')
distance_matrix = calculateDistances(populated_centers)


TSP(distance_matrix,populated_centers,0)

