import numpy as np

DEBUG = True

def log(str):
    if DEBUG:
        print(str)

def getXY(items):
    result = []
    xy = items.split(',')
    result.append(int(xy[0]))
    result.append(int(xy[1]))
    return result

def getPos(line):
    items = line.split('->')
    result = [[]*2]*2

    result[0] = getXY(items[0])
    result[1] = getXY(items[1])
    log(result)
    return result

def getResult(items):
    grids = np.array(items)

    print(grids)

    count = np.amax(grids)

    arr = np.zeros((count+1, count+1))
    for i in range(len(grids)):
        a = grids[i][0]
        b = grids[i][1]
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                arr[a[0]][y] += 1
        else:
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                arr[x][a[1]] += 1

    print(arr)
    print(np.count_nonzero(arr > 1))

with open('day5/input') as file:
    grids = []
    while True:
        line = file.readline()

        if not line:
            break

        vent = getPos(line)

        if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
            grids.append(getPos(line))

    getResult(grids)
    file.close()

