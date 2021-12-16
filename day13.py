import numpy as np

DEBUG = False

DIRECTS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
def log(str):
    if DEBUG:
        print(str)

def getSize(lines):
    x = 0
    y = 0
    for line in lines:
        if line == '\n':
            break
        items = line.strip().split(',')
        x = max(x, int(items[0]))
        y = max(y, int(items[1]))

    return [x, y]

def processBoard(lines, arr):
    index = 0
    for line in lines:
        index += 1
        if line == '\n':
            break
        items = line.strip().split(',')
        log(formatPos(int(items[1]), int(items[0])))
        arr[int(items[1])][int(items[0])] = '#'

    log(arr)
    rows = len(arr)
    cols = len(arr[0])
    log(formatPos(rows, cols))
    log(lines[index])

    while index < len(lines):
        log(formatPos(index, len(lines)))
        command = lines[index].strip().split('=')
        if command[0] == 'fold along x':
            x = int(command[1])
            result = foldX(arr, x, rows, cols)
            cols = x
        else:
            y = int(command[1])
            result = foldY(arr, y, rows, cols)
            rows = y

        arr = np.array(result)
        log(arr)
        index += 1
        # break

    prinfArray(arr, rows, cols)
    print(len(np.where(arr == '#')[0]))

def foldX(arr, x, rows, cols):
    for i in range(rows):
        for j in range(x, cols):
            if arr[i][x - (j-x)] == '.' and arr[i][j] == '#':
                arr[i][x - (j-x)] = '#'
    log('foldX')
    return arr[:rows,:x]

def foldY(arr, y, rows, cols):
    for j in range(cols):
        for i in range(y, rows):
            if arr[y - (i-y)][j] == '.' and arr[i][j] == '#':
                arr[y - (i-y)][j] = '#'
    log('foldY')
    return arr[:y,:cols]

def parseAlline(file):
    lines = file.readlines() 
    size = getSize(lines)

    board = [['.'] * (size[0]+1)] * (size[1]+1)
    processBoard(lines, np.array(board))

def prinfArray(arr, rows, cols):
    for i in range(rows):
        line = ''
        for j in range(cols):
            line += arr[i][j]
        print line

def formatPos(i, j):
    return '('+str(i)+','+str(j) + ')'

with open('day13/input') as file:
    parseAlline(file)

    file.close()


