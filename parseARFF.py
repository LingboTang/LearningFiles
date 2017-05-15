import os
import random

def main():
    newData = []
    f = open("validate2.arff",'r')
    of = open("myTest2.txt",'w')
    for line in f:
        newData.append(line.split())
    dataStartIndex = newData.index(["@DATA"])
    attributes = newData[:dataStartIndex]
    Data = newData[dataStartIndex+1:]
    random.shuffle(Data)
    f.close()
    for line in Data:
        lineString = ', '.join(line)
        of.write(lineString+"\n")
    of.close()

main()
