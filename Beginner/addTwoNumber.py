#!/usr/bin/env python3
def readTotaltestcase():
    totalTestcase = int(input())
    return(totalTestcase)
def sumList(totalTestCase):
    totalList = []
    for values in range(0,totalTestCase):
        number1,number2 = map(int,input().split())
        totalList.append(number1+number2)
    return(totalList)
def printResult(total):
    for i  in total:
        print(i)
if __name__ == "__main__":
        totalTestcase = readTotaltestcase()
        total = sumList(totalTestcase)
        printResult(total)
