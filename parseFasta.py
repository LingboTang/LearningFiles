import os
import random

Exon_type_A = [7, 21, 36, 45, 60, 9, 24, 37, 47, 61, 11, 25, 38, 51, 66, 17, 26, 39, 53, 75, 18, 30, 41, 54, 76, 19, 35, 42, 59, 77]

Exon_type_B = [27]

Exon_type_C = [4, 15, 29,44, 56, 67, 5, 15, 31, 46, 57, 68, 6, 16, 32, 48, 58, 69, 8, 20, 33, 49, 62, 71, 10, 22, 34, 50, 63, 72, 12, 23, 40, 52, 64, 73, 13, 28, 43, 55, 65, 74]

Exon_type_D = [2, 3]

Exon_type_E = [70, 78]

def main():
    newData = []
    f = open("journal.pone.0120058.s011.FASTA",'r')
    of = open("whichType.txt",'w')
    for line in f:
        newData.append(line.split())
    f.close()
    for line in newData:
        if (len(line) == 0):
            newData.remove(line) 
    for line in newData:
        if (line[0][0] == '>'):
            if (int(line[0][6:8]) in Exon_type_A):
                of.write("A\n")
            elif (int(line[0][6:8]) in Exon_type_C):
                of.write("C\n")
            else:
                pass
    of.close()

main()
