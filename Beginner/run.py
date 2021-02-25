import itertools
#carpaths = 4 rue-de-londres rue-d-amsterdam rue-de-moscou rue-de-rome
def sortBusyRoads(carPaths, roads):
    criticalPath = {}
    sortedPaths = []
    for carPath in carPaths:
        paths = carPath.split(' ')[2:] #car waiting at the end of the first road
        for path in paths:
            criticalPath[path] = criticalPath.get(path, 0) + 1
    for name, frequency in criticalPath.items():
        sortedPaths.append((name, frequency, roads[name]))
    
    return criticalPath
    #sorted(sortedPaths, key = lambda x : x[1], reverse=True)
    
# roads = 
def processJunctions(roads):
    intersectionIncomingMap = {}
    intersectionOutgoingMap = {}
    for name, value in roads.items():
        if value[0] in intersectionOutgoingMap:
            intersectionOutgoingMap[value[0]].append(name)
        else:
            intersectionOutgoingMap[value[0]] = [name]
        
        if value[1] in intersectionIncomingMap:
            intersectionIncomingMap[value[1]].append(name)
        else:
            intersectionIncomingMap[value[1]] = [name]
    return (intersectionIncomingMap, intersectionOutgoingMap)

def process(carPaths, roads):
    criticalPath = sortBusyRoads(carPaths, roads)
    print(criticalPath)
    intersectionIncomingMap, intersectionOutgoingMap = processJunctions(roads)
    outputs = []
    for junctionid, incomingRoads in roads.intersectionIncomingMap():
        temp = []
        for road in incomingRoads:
            if road in criticalPath:
                temp.append(road, criticalPath[road])
        outputs.append(junctionid, temp)

    return outputs

def readInput():
    inputFile = open("C:\\Users\\deblghosh\\OneDrive - Lexmark\\Chrome\\a.txt", "r")
    firstLine = inputFile.readline()
    streetList = []
    streetMap = {}
    carPath = []
    if firstLine:
        simulation, intersection, streets,cars,scores = map(int,firstLine.split())
    for line in itertools.islice(inputFile, 0, int(streets)):
        streetList.append(line.strip())
    streetMap=processInput(streetList)
    for line in itertools.islice(inputFile, 0, int(cars)):
        carPath.append(line.strip()[1:])

    return(simulation,intersection,streetMap,carPath)

def processInput(streetList):
    streetMap = {}
    for street in streetList:
        roadName =(street.split(' ')[2])
        streetMap[roadName] = [int(street.split(' ')[0]),int(street.split(' ')[1]),int(street.split(' ')[3])]
    return(streetMap)

def processOutput(output):
    out = open(f'C:\\Users\\deblghosh\\OneDrive - Lexmark\\Chrome\\aOut.txt', 'w')
    out.write(str(len(output)) + "\n")
    for line in output:
        out.write(str(line[0]) + "\n")
        out.write(str(len(line[1])) + "\n")
        for roadName, cycle in line[1]:
             out.write(roadName+ " " + cycle + "\n")
    out.close()

if __name__ == '__main__':
    simtime, totalIntersections, roads, carPaths = readInput()
    output = process(carPaths, roads)
    processOutput(output)
    