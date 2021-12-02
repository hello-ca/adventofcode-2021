file = open('day1/input', 'r')
count = 0
pre = file.readline()
while pre:
    line = file.readline()
 
    if not line:
        break
    
    if line > pre:
        count += 1

    pre = line

print(count)
file.close()