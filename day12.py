import numpy as np

DEBUG = False

BIG = set()
SMALL = set()
S_VISITED = set()
ADJ_MAP = {}

Start = 'start'
End = 'end'
result = 0
result2 = 0

def log(str):
    if DEBUG:
        print(str)

def checkMap(map, item):
    if not item in map:
        map[item] = set()

def buildAdj(items1, items2):
    checkMap(ADJ_MAP, items1)
    ADJ_MAP[items1].add(items2)
    checkMap(ADJ_MAP, items2)
    ADJ_MAP[items2].add(items1)
    if items1.islower() and items1 != Start and items1 != End:
        SMALL.add(items1)

    if items2.islower() and items2 != Start and items2 != End:
        SMALL.add(items2)

def dfs(cur, path, visited):
    # path.add(cur)
    # log(cur)
    if cur.islower():
        if cur in visited:
            return

        visited.add(cur)

    path.append(cur)
    if cur == End:
        global result;
        result += 1
        log("found")
        log(path)
  
    for next in ADJ_MAP[cur]:
        if next == Start or next in visited:
            continue
        # print(next)
        dfs(next, path, visited)
        if next.islower():
            visited.remove(next)

    path.pop()

def buildVisit():
    visited = dict()
    for small in SMALL:
        visited[small] = 0

    return visited

def checkSmall(visited):
    count = 0
    for key in visited.keys():
        if visited[key] > 1:
            count += 1
    return count

def dfs2(start, end, path, visited):
    log(start + '->' + end)
    
    if start.islower():
        visited[start] += 1
        if checkSmall(visited) > 1:
            return

    # print(visited)
    path.append(start)
    if start == end:
        global result2;
        result2 += 1
        log("found")
        log(visited)
        log(path)
        log('found ----')
  
    for next in ADJ_MAP[start]:
        if next == Start or next == End:
            continue

        if next in visited.keys():
            if visited[next] == 2:
                continue

            if checkSmall(visited) == 1 and visited[next] > 0:
                continue

        dfs2(next, end, path, visited)
        if next.islower():
            visited[next] -= 1

    path.pop()

def parseAlline(file):
    while True:
        line = file.readline()

        if not line:
            break;

        items = line.replace('\n', '').split('-')
        log(items)
        buildAdj(items[0], items[1])

    log(SMALL)
    log(ADJ_MAP)

    # Part 1
    dfs(Start, [], set())

    # Part 2
    for start in ADJ_MAP[Start]:
        for end in ADJ_MAP[End]:
            dfs2(start, end, [], buildVisit())

with open('day12/input') as file:
    parseAlline(file)
    print(result)
    print(result2)
    file.close()


