import csv

def readCE(filename):
    dictionary = {}
    with open(filename, encoding='utf-8-sig') as csvfile:
        file = csv.reader(csvfile, delimiter=',')

        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["id"]=row[0]
                elem["name"] = row[1]
                elem["distrito"] = row[3]
                elem["xCord"] = float(row[5])
                elem["yCord"] = float(row[6])
                dictionary[idelem] = elem
                del elem
            idelem += 1
        

    return dictionary