import itertools
def readInput():
    inputFile = open("a.txt", "r")
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
if __name__ == "__main__":
    inputList = readInput()

