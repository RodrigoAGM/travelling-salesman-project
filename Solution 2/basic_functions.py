import csv

def readCSV(filename):
    """
    Function that recieves a filename, reads that csv file and returns a dictionary
    of arrays grouped by the department of the elements and with the name, xcord and 
    ycord of each populated center of the file. Also, the dunction returs an array 
    containing all the departments.
    """
    dictionary = {}
    places = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["xCord"] = float(row[15])
                elem["yCord"] = float(row[16])
                if row[1] not in dictionary:
                    dictionary[row[1]] = []
                    dictionary[row[1]].append(elem)
                    places.append(row[1])
                else:
                    dictionary[row[1]].append(elem)

                del elem
            
            idelem += 1
    
    return dictionary, places

def calculateDistances(dictionary, department):
    """
    Function that recieves an dictionary od populated centers and a department
    to generate a distance matrix for all the possible connections between two pairs of 
    populated centers from the same department.
    """
    distance_matrix = []
    row = []
    n = len(dictionary[department])
    for fil in range(n):
        for col in range(n):
            if fil == col:
                row.append(0)
            else:
                operation = ((dictionary[department][col]["xCord"]) - (dictionary[department][fil]["xCord"]))**2 + ((dictionary[department][col]["yCord"] - dictionary[department][fil]["yCord"]))**2
                distance = operation**0.5
                row.append(distance)
        distance_matrix.append(row)
        row = []
    return distance_matrix

def calculateDistancesDictionary(dictionary, departments):
    """
    Function that generates a dictionary of distances organized by departments
    """
    n = len(departments)
    distance_dictionary = {}

    for pos in range(n):
        dep = departments[pos]
        distance_dictionary[dep] = calculateDistances(dictionary, dep)

    return distance_dictionary
