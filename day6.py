import numpy as np
from datetime import datetime

DEBUG = True
def log(str):
    if DEBUG:
        print(str)

def getFishes(line):
    items = line.replace('\n', '').split(',')
    log(items)
    fishes = []
    for item in items:
        # log(item)
        fishes.append(int(item))
    
    return fishes

def genFish(fishes, days):
    for i in range(days):
        totals = len(fishes)
        for j in range(totals):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
            else:
                fishes[j] -= 1

    print(len(fishes))

def genFish2(days):
    fishes = np.full(6000000000, -1, dtype=np.int8)
    fishes[0] = 4
    # fishes[1] = 4
    # fishes[2] = 3
    # fishes[3] = 1
    # fishes[4] = 2
    total = 1
    
    print("start =", datetime.now())
    for i in range(days):
        # print(fishes[:total])
        zeros = np.argwhere(fishes[:total] == 0)
        # nonzeros = np.nonzero(fishes[:total] > 0)
        # fishes[nonzeros] -= 1
        for j in range(total):
            if (fishes[j] > 0):
                fishes[j] -= 1
        
        if len(zeros) > 0:
            # print(zeros)
            fishes[zeros] = 6
            fishes[total:total+len(zeros)] = 8
            total += len(zeros)
        # print(fishes[:total])

    print("end =", datetime.now())
    print('fish 4 after ' + str(days) + ", would be:" + str(total))

with open('day6/input2') as file:
    fishes = []
    line = file.readline()

    fishes = getFishes(line)

    # For part 1
    # genFish(fishes, 256)

    # For part 2
    genFish2(256)
    
    file.close()


