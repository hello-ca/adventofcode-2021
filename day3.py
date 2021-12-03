#part 1
BITSIZE = 12
with open('day3/input') as file:
    cal = [0] *  BITSIZE
    total = 0
    while True:
        line = file.readline()
     
        if not line:
            break

        total += 1
        for x in range(BITSIZE):
            if line[x] == '1':
                cal[x] += 1
        
    gamma = 0
    epsilon = 0
    print(cal)
    for x in range(BITSIZE):
        if cal[x] > total - cal[x]:
            gamma += (1 << (BITSIZE - x - 1))
        else:
            epsilon += (1 << (BITSIZE - x - 1))


    print(str(gamma) + "," + str(epsilon))
    print(gamma*epsilon)
    file.close()


#part 2
def checkBit(number, bit, flag):
    return number[bit] == flag

def getBitOne(lines, pos):
    count = 0
    for line in (lines):
        if line[pos] == '1':
            count += 1;

    return count

def changeBit(lines, pos, val):
    newlines = []
    for line in (lines):
        newlines.append(line[:pos] + val + line[pos+1:])

    return newlines

def getrating(lines, isoxygen):
    result = ''
    for x in range(BITSIZE):
        onetotal = getBitOne(lines, x)
        check = '0'
        if onetotal > len(lines) - onetotal:
            check = '1' if isoxygen else '0'
        elif onetotal == len(lines) - onetotal:
            check = '1' if isoxygen else '0'
            #lines = changeBit(lines, x, '1' if isoxygen else '0')
        else:
            check = '0' if isoxygen else '1'


        newlines = list(filter(lambda number: checkBit(number, x, check), lines))
        # print(newlines)
        if len(set(newlines)) == 1:
            result = newlines[0]
            break;
        lines = newlines

    print('answer:' + result)
    return result

with open('day3/input') as file:
    lines = file.readlines()
    oxygen = int(getrating(lines, True), 2)
    co2 = int(getrating(lines, False), 2)

    print('oxygen:' + str(oxygen) + ",co2:" + str(co2))
    print(oxygen * co2)
    file.close()