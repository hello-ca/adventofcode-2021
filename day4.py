import numpy as np

DEBUG = False

def log(str):
    if DEBUG:
        print(str)

#part 1
GRIDSIZE = 5
def getGrids(file):
    total = 0
    grids = []
    while True:
        line = file.readline()
     
        if not line:
            break

        if line == '\n':
            continue

        if (total % GRIDSIZE == 0):
            grid = [[]*GRIDSIZE]*GRIDSIZE

        grid[total % GRIDSIZE] = list(map(int, line.split()))
        total += 1

        if (total % GRIDSIZE == 0):
            grids.append(grid)
    return grids


def checkGrids(grids, numbers):
    #part 1
    print('---Part 1---')
    result = [[-1]*2] * len(grids)
    all_index = len(numbers) + 1
    score = 0
    for i in range(len(grids)):
        result[i] = checkGrid(grids[i], numbers)
        if result[i][0] < all_index:
            all_index = result[i][0]
            score = result[i][1]

    log(result)
    print(score)
    print(all_index)

    #part 2
    print('---Part 2---')
    all_index = 0
    for i in range(len(grids)):
        if result[i][0] > all_index:
            all_index = result[i][0]
            score = result[i][1]

    print(score)

def checkGrid(grid, numbers):
    newgrid = np.array(grid)

    tmp = np.array(grid)
    log(numbers)
    found = -1
    
    for j in range(0, len(numbers)):
        tmp[tmp == numbers[j]] = -1
        for i in range(GRIDSIZE):
            # print(numbers[j])
            if np.all(tmp[i] ==  -1):
                log('found row:' + str(j))
                found = j
                break;

            if np.all(tmp[:, i] ==  -1):
                log('found col:' + str(j))
                found = j
                break;

        if found > -1:
            break


    # print(tmp)
    tmp[tmp == -1] = 0  
    log('-------' + str(numbers[found]) + ',sum:' + str(tmp.sum()))
    # print(tmp)
    return [found, numbers[found] * tmp.sum()]

with open('day4/input') as file:
    line = file.readline().replace('\n', '')
    numbers = []
    log(line)
    items = line.split(',')
    # numbers = np.empty([len(items)])
    for item in items:
        numbers.append(int(item))

    log(numbers)
    np_numbers = np.array(numbers);
    log(np_numbers)

    grids = getGrids(file)
    checkGrids(grids, np_numbers)

    
    log(grids)
    log(grids[0][0][1])
    file.close()

