import sys, os
from random import randint, shuffle
import argparse
STDERR = sys.stderr

parser = argparse.ArgumentParser(description="Create a random list of pairs of students with the conditions that two students of the same year should not pair.")
parser.add_argument('listname', nargs="+", help="List of students")

args = parser.parse_args()

##MN will be the program with the least number of students
##MJ will be the program with the greater number of students
MN = []
MJ = []

BPS = []
BMI = []

with open(sys.argv[1], 'r') as studentlist:
    for line in studentlist:
        student=line.strip("\n").split(",")
        if(student[3] == "BP" or student[3] == "Biophysics"):
            BPS.append(student[0:4])
        elif(student[3] == "BMI" or student[3] == "Bioinformatics"):
            BMI.append(student[0:4])

###Check which program has the greater number of students
if len(BPS) > len(BMI):
    MJ = BPS
    MN = BMI
else:
    MJ=BMI
    MN=BMI


shuffle(MJ)
shuffle(MN)

mjn = len(MJ)
mnn = len(MN)

while mjn != 0:

    while mnn != 0:
        rnd1 = randint(0, mjn - 1)
        rnd2 = randint(0, mnn - 1)
        ntr = 0
        while MJ[rnd1][2] == MN[rnd2][2] and ntr < 10:
            rnd2 = randint(0, mnn -1)
            ntr = ntr + 1
        print "{0:33} {1}".format(",".join(MJ[rnd1]), ",".join(MN[rnd2]))
        del MJ[rnd1]
        del MN[rnd2]
        mjn = len(MJ)
        mnn = len(MN)

    else:
        if mjn > 1:
            rnd1 = randint(0, mjn - 1)
            tmp = ",".join(MJ[rnd1])
            del MJ[rnd1]
            mjn = len(MJ)
            rnd2 = randint(0, mjn - 1)
            print "{0:33} {1}".format(tmp,",".join(MJ[rnd2]))
            del MJ[rnd2]
            mjn = len(MJ)

        else:
            print ",".join(MJ[0])
            mjn = 0




