
file = open('day1/input', 'r')
count = 0
pre = file.readline()
while pre:
    line = file.readline()
 
    if not line:
        break
    
    if line > pre:
        count += 1

print(f"Part 1: {count}")
file.close()