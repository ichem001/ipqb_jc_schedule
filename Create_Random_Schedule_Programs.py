import sys, os
from random import randint, shuffle

BPS = []
BMI = []
with open(sys.argv[1], 'r') as studentlist:
    for line in studentlist:
        student=line.strip("\n").split(",")
        if(student[4] == "Biophysics"):
            BPS.append(student[0:4])
        elif(student[4] == "Bioinformatics"):
            BMI.append(student[0:4])

shuffle(BPS)
shuffle(BMI)

ub1 = len(BPS)
ub2 = len(BMI)

while ub1 != 0:

    while ub2 != 0:
        rnd1 = randint(0, ub1 - 1)
        rnd2 = randint(0, ub2 - 1)
        ntr = 0
        while BPS[rnd1][2] == BMI[rnd2][2] and ntr < 10:
            rnd2 = randint(0, ub2 -1)
            ntr = ntr + 1
        print(BPS[rnd1], "     ", BMI[rnd2])
        del BPS[rnd1]
        del BMI[rnd2]
        ub1 = len(BPS)
        ub2 = len(BMI)

    else:
        if ub1 > 1:
            rnd1 = randint(0, ub1 - 1)
            tmp = BPS[rnd1]
            del BPS[rnd1]
            ub1 = len(BPS)
            rnd2 = randint(0, ub1 - 1)
            print(tmp, "     ", BPS[rnd2])
            del BPS[rnd2]
            ub1 = len(BPS)

        else:
            print(BPS[0])
            ub1 = 0




