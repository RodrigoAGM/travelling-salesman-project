import csv

def readFile(filename):
   
    dictionary = {}
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        idelem = -1

        for row in file:
            if idelem != -1:
                elem = {}
                elem["name"] = row[0]
                elem["xCord"] = float(row[1])
                elem["yCord"] = float(row[2])
                dictionary[idelem] = elem
                del elem
            
            idelem += 1
    #print(dictionary[0]["name"]) -> Huamampallpa
    return dictionary


def point_dist(self, x1,y1,x2,y2):      
    readFile('Book4.csv')   
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)