#part 1
import re
DIRECT = {'forward':[1, 0], 'down':[0, 1], 'up':[0, -1]}

with open('day2/input') as file:
    x = 0
    y = 0
    while True:
        line = file.readline()
     
        if not line:
            break

        items = line.split(' ')
        action = items[0];
        step = int(items[1]);

        # print(step)

        x += DIRECT[action][0] * step
        y += DIRECT[action][1] * step
    print(x*y)
    file.close()

#part 2
with open('day2/input') as file:
    x = 0
    y = 0
    aim = 0
    while True:
        line = file.readline()
     
        if not line:
            break

        items = line.split(' ')
        action = items[0];
        step = int(items[1]);


        x += DIRECT[action][0] * step
        aim += DIRECT[action][1] * step

        if action == 'forward':
            y += abs(step) * aim
        # print('test:' + str(y) + "," + str(aim))
    print(x*y)
    file.close()
