# import numpy as np
# import sys


BONUS = {')':3, ']':57, '}':1197, '>':25137}
PAIRS = {'(':')', '[':']', '{':'}', '<':'>'}

BONUS_2 = {')':1, ']':2, '}':3, '>':4}
DEBUG = False
def log(str):
    if DEBUG:
        print(str)

part2score = []
def checkLine(line):
    stack = []
    for c in line:
        if c in PAIRS.values():
            if len(stack) == 0 or PAIRS[stack[-1]] != c:
                return c

            if len(stack) > 0 or PAIRS[stack[-1]] == c:
                stack.pop()
        else:
            stack.append(c)

    if len(stack) > 0:
        c = stack[-1]
        countPart2(stack)
        return c

    return 'o'

def countPart2(stack):
    result = 0

    print(stack)
    while len(stack) > 0:
        c = stack[-1]
        result *= 5
        result += BONUS_2[PAIRS[c]]
        stack.pop()

    part2score.append(result)
    print(result)

def parseAlline(file):
    result = 0
    print(PAIRS.values())
    print(PAIRS.keys())
    while True:
        line = file.readline().replace('\n', '').strip()

        if not line:
            break;

        key = checkLine(line)
        print(key)

        if key in BONUS.keys():
            result += BONUS[checkLine(line)]
        

    print(result)

def formatPos(i, j):
    return '('+str(i)+','+str(j) + ')'

with open('day10/input') as file:
    parseAlline(file)
 
    part2score.sort()
    mid = len(part2score) / 2
    print(mid)
    print(part2score[mid])
    file.close()


