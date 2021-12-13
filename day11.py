import numpy as np

DEBUG = False

DIRECTS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
def log(str):
    if DEBUG:
        print(str)

def toArray(lines, rows,  cols):
    result = np.zeros((rows, cols))
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = ord(lines[i][j]) - ord('0')

    print(result)
    return result

def checkUpdate(arr, i, j, rows, cols):
    for direct in DIRECTS:
        x = i + direct[0]
        y = j + direct[1]
        if x < 0 or y < 0 or x >= rows or y >= cols:
            continue

        arr[x][y] += 1

def updateArray(arr, indexes, val):
    for index in indexes:
        arr[index[0]][index[1]] = val

def flashes(arr, rows, cols):
    arr += 1

    flag = np.array([[False]*cols]*rows)
    toUpdate = np.argwhere(arr>9)
    while True:
        for item in toUpdate:
            checkUpdate(arr, item[0], item[1], rows, cols)

        updateArray(flag, toUpdate, True)
        newToUpdate = np.argwhere(arr>9)

        if len(newToUpdate) == len(np.argwhere(flag==True)):
            break

        log(flag)
        newNines = []
        for item in newToUpdate:
            if not flag[item[0]][item[1]]:
                newNines.append(item)
        toUpdate = np.array(newNines)
        # print toUpdate
    arr[arr>9] = 0

def parseAlline(file, steps):
    lines = file.readlines()
    result = 0
    rows = len(lines)
    cols = len(lines[0]) - 1
    arr = toArray(lines, rows, cols)

    for i in range(steps):
        flashes(arr, rows, cols)
        log(i)
        log(arr)
        cur = len(np.argwhere(arr==0))
        if cur == rows * cols:
            print('***found:' + str(i+1))
        result += len(np.argwhere(arr==0))

    print(result)

def formatPos(i, j):
    return '('+str(i)+','+str(j) + ')'

with open('day11/input') as file:
    parseAlline(file, 500)

    file.close()


