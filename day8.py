import numpy as np
import sys

KEY_NUM = {2:1, 3:7, 4:4, 7:8}


SYMBOLS_2 = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
DEBUG = False
def log(str):
    if DEBUG:
        print(str)

def printSymbols(symbol):
    for line in symbol:
        print(line)

def parseLine(line):
    groups = line.split('|')
    items = groups[1].strip().split(' ')

    count = 0
    for item in items:
        # print(item.strip())
        key = len(set(item.strip()))
        if key in KEY_NUM.keys():
            count += 1

    # print(count)
    return count

def parseAlline(file):
    count = 0
    while True:
        line = file.readline()

        if not line:
            break;
        count += parseLine(line)

    print(count)

def parseLine2(line):
    groups = line.split('|')
    items = groups[1].strip().split(' ')

    number = guessNumber(groups[0].strip().split(' '), groups[1].strip().split(' '))
    # count = 0
    # for item in items:
        

    # print(count)
    return number

def guessNumber(items, targets):
    uniqueNumber = [];
    uniqueMap = dict()
    for item in items:
        tmp = list(item.strip())
        # print(tmp)
        if len(tmp) in KEY_NUM.keys():
            uniqueMap[KEY_NUM[len(tmp)]] = tmp

    guessmap1 = [{}]*8

    # print(uniqueMap)

    candidate7 = list(set(uniqueMap[7]) - set(uniqueMap[1]))
    candidate4 = list(set(uniqueMap[4]) - set(uniqueMap[7]) - set(uniqueMap[1]))
    candidate8 = list(set(uniqueMap[8]) - set(uniqueMap[4]) - set(uniqueMap[7]))
    # print(candidate8)
    # print(candidate4)
    # print('-----')
    
    number = 0
    for i in range(2):
        myguess = dict()
        myguess[candidate7[0]] = 'a'
        myguess[uniqueMap[1][i]] = 'c'
        myguess[uniqueMap[1][(i+1)%2]] = 'f'
        for j in range(2):
            myguess[candidate4[j]] = 'b'
            myguess[candidate4[(j+1)%2]] = 'd'
            for k in range(2):
                myguess[candidate8[k]] = 'e'
                myguess[candidate8[(k+1)%2]] = 'g'
                if validGuess(items, myguess):
                    print('found')
                    print(myguess)
                    number += decodeNumber(myguess, targets)

    # validGuess(guessmap1)
    # for num in [1, 4, 7, 8]:

        

    return number
    # print(uniqueMap)

def validGuess(items, myguess):
    # print(myguess)
    for item in items:
        # print(item)
        target = toNumber(item, myguess)
        
        if not target in set(SYMBOLS_2):
            return False

    return True

def toNumber(value, myguess):
    target = ""
    for c in value:
        target += myguess[c]

    target = ''.join(sorted(target))
    return target

def decodeNumber(myguess, numbers):
    result = 0
    print(myguess)
    print(numbers)
    for number in numbers:
        log('**checking**')
        log(number)
        target = toNumber(number, myguess)
        log(target)
        for i in range(len(SYMBOLS_2)):
            if target == SYMBOLS_2[i]:
                log(i)
                result = result*10 + i
                break
        log(result)

    log(result)
    return result

def parseAlline2(file):
    print('test')

    count = 0
    while True:
        line = file.readline()

        if not line:
            break;

        count += parseLine2(line)

    print(count)


with open('day8/input') as file:
    # For part 1
    # parseAlline(file)

    # For part 2
    parseAlline2(file)
    
    file.close()


