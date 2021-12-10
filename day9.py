import numpy as np
import sys
import queue

DIRECT = [-1, 0, 1, 0, -1]
DEBUG = False
def log(str):
    if DEBUG:
        print(str)

def lineToNums(line):
    nums = [10]*(len(line)+2)
    log(line)
    for i in range(len(line)):
        nums[i+1] = ord(line[i]) - ord('0')

    return nums;

def parseAlline(file):
    rows = []
    result = 0
    firstLine = True
    lineLen = 0
    while True:
        line = file.readline().replace('\n', '').strip()
        if firstLine:
            firstLine = False
            lineLen = len(line)
            rows.append([10]*(lineLen + 2))

        if not line:
            break;

        nums = lineToNums(line)
        rows.append(nums)

    rows.append([10]*(lineLen + 2))
    return rows

def findLow(orirows):
    rows = np.array(orirows)
    # print(rows)
    result = 0
    row_nums = len(rows)
    col_nums = len(rows[0])

    for i in range(1, row_nums - 1):
        for j in range(1, col_nums - 1):
            islow = True
            for k in range(len(DIRECT) - 1):
                adj_x = i + DIRECT[k]
                adj_y = j + DIRECT[k+1]

                if rows[i][j] >= rows[adj_x][adj_y]:
                   islow = False
                   break; 

            if islow:
                # print('found')
                # print(rows[i][j])
                result += rows[i][j] + 1


    return result

def findBasins(orirows):
    rows = np.array(orirows)

    result = 0
    row_nums = len(rows)
    col_nums = len(rows[0])
    log(str(row_nums) +"," + str(col_nums))
    basins = []
    
    flags = np.array([[False]*110]*110)
    for i in range(1, row_nums - 1):
        for j in range(1, col_nums - 1):
            if not flags[i][j] and rows[i][j] < 9:
                q = queue.Queue()
                q.put([i, j]);
                count = 0
                log('queue start:' + str(i) + ',' + str(j))
                while not q.empty():
                    cur = q.get()
                    flags[cur[0]][cur[1]] = True
                    count += 1
                    for k in range(len(DIRECT) - 1):
                        x = cur[0] + DIRECT[k]
                        y = cur[1] + DIRECT[k+1]
                        if x < 1 or x >= row_nums - 1 or y < 1 or y >= col_nums - 1:
                            continue

                        if rows[x][y] == 9 or flags[x][y]:
                            continue

                        log(str(k) + ':' + formatPos(cur[0],cur[1]) + '->' + formatPos(x, y))
                        flags[x][y] = True
                        q.put([x, y])
                
                log('queue end:' + str(count))
                basins.append(count)

    basins.sort(reverse=True)
    log(basins) 
    print(basins[0] * basins[1] * basins[2])

def formatPos(i, j):
    return '('+str(i)+','+str(j) + ')'

with open('day9/input') as file:
    rows = parseAlline(file)
    # For part 1
    print(findLow(rows))

    # For part 2
    print(findBasins(rows))
    
    file.close()


