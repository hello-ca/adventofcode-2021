with open('day1/input') as file:
    count = 0
    pre = file.readline()
    while pre:
        line = file.readline()
     
        if not line:
            break
        
        if line > pre:
            count += 1

        pre = line

    # print(count)
    print(f'Part 1: {count}')
    file.close()