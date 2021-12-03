#part 1
with open('day1/input') as file:
    count = 0
    pre = ""
    while True:
        line = file.readline()
     
        if not line:
            break

        if pre and int(line) > int(pre):
            count += 1

        pre = line

    print(count)
    file.close()

#part 2
with open('day1/input') as file:
    SIZE = 3
    count = 0
    numbers = 0
    window = [0] * SIZE; 
    while True:
        line = file.readline()
     
        if not line:
            break

        cur = int(line)
        if numbers >= SIZE:
            if window[0] < cur:
                count += 1
            window[0] = window[1]
            window[1] = window[2]
            window[2] = cur
        else:
            window[numbers] = cur;

        numbers += 1

    print(count)
    file.close()
