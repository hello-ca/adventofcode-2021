import numpy as np
import sys

from datetime import datetime

DEBUG = True
def log(str):
    if DEBUG:
        print(str)

def getGrabs(line):
    items = line.replace('\n', '').split(',')
    count = len(items)
    grabs = np.zeros(count)
    log(items)
    for i in range(count):
        # log(item)
        grabs[i] = int(items[i])
    
    return grabs

def getBestCost(grabs):
    cost = sys.maxint
    for i in range(len(grabs)):
        tmp = np.copy(grabs)
        tmp -= grabs[i]
        cost = min(cost, np.absolute(tmp).sum())

    print(cost)
    return cost

def getBestCost2(grabs):
    cost = sys.maxint
    maxpos = int(np.amax(grabs))
    for i in range(maxpos + 1):
        tmp = np.copy(grabs)
        for j in range(len(grabs)):
            steps = abs(tmp[j] - i)
            tmp[j] = int((steps + 1) * steps) >> 1
        cost = min(cost, np.absolute(tmp).sum())

    print(cost)
    return cost   

with open('day7/input') as file:
    line = file.readline()

    # For part 1
    grabs = getGrabs(line)
    getBestCost(grabs)

    # For part 2
    getBestCost2(grabs)
    
    file.close()


