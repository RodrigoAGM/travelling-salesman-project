import csv

def readCSV(filename):
    """
    Function that recieves a filename, reads that csv file and returns a dictionary with 
    the name, xcord and ycord of each populated center of the file. 
    """
    dictionary = {}
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["xCord"] = float(row[15])
                elem["yCord"] = float(row[16])
                dictionary[idelem] = elem
                del elem
            
            idelem += 1
    
    return dictionary

def calculateDistances(dictionary):
    """
    Function that recieves a dictionary of data and generates a distance matrix for all
    the possible connections between two pairs of populated centers
    """
    distance_matrix = []
    row = []
    n = len(dictionary)
    #n = 10
    for fil in range(n):
        for col in range(n):
            if fil == col:
                row.append(0)
            else:
                operation = ((dictionary[col]["xCord"]) - (dictionary[fil]["xCord"]))**2 + ((dictionary[col]["yCord"] - dictionary[fil]["yCord"]))**2
                distance = operation**0.5
                row.append(distance)
        distance_matrix.append(row)
        row = []
    return distance_matrix

#D = readCSV('dataset.csv')
#distances = calculateDistances(D)
#print(distances)
