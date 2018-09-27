import csv

def readCSV1(filename):
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

def calculateDistances(array):
    """
    Function that recieves an array of dictionaries and generates a distance matrix for all
    the possible connections between two pairs of populated centers.
    """
    distance_matrix = []
    row = []
    n = len(array)
    #n = 1000
    for fil in range(n):
        for col in range(n):
            if fil == col:
                row.append(0)
            else:
                operation = ((array[col]["xCord"]) - (array[fil]["xCord"]))**2 + ((array[col]["yCord"] - array[fil]["yCord"]))**2
                distance = operation**0.5
                row.append(distance)
        distance_matrix.append(row)
        row = []
    return distance_matrix
