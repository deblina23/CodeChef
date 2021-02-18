def readInput():
    inputList = []
    for _ in  range(int(input())):
        inputList.append(int(input()))
    return(inputList)
def result(inputList):
    inputList.sort()
    for result in inputList:
        print(result)

if __name__ == "__main__":
    inputList = readInput()
    result(inputList)