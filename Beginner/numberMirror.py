#!/usr/bin/env python3
def readNumber():
    number = int(input())
    return(number)
def checkRange(number):
    if (number>=0 and number<=pow(10,5)):
        return(True)

def printNumber(number):
    if(checkRange):
        print(number)

if __name__ == "__main__":
    number = readNumber()
    print(number)
        
