import csv

def readCSV(filename):
    dictionary = {}
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[5]
                elem["xCord"] = row[15]
                elem["yCord"] = row[16]
                dictionary[idelem] = elem
                del elem
            
            idelem += 1
    
    return dictionary



