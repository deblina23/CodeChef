#!/usr/bin/env python3
def readInput():
    n,k = map(int,(input().split()))
    listData = []
    for number in range(0,n):
        listData.append(int(input()))
    return(k,listData)
def resultCalculation(data):
    result = 0
    k,listData = tuple(value for value in data)
    if(k<=pow(10,7)):
        for number in listData:
            if((number<=(pow(10,9))) and ((number%k)==0)):
                result =result+1
    return(result)
def printResult(result):
    print(result)
if __name__ == "__main__":
    readData = readInput()
    result = resultCalculation(readData)
    printResult(result)
            
