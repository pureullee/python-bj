import sys

n = int(input())

count = 0

for i in range(n) :
    line = sys.stdin.readline().rstrip()
    check =[]
    while len(line) != 0 :
        
        if line[0] not in check :
            check.append(line[0])
            line = line.lstrip(line[0])
        
        else :
            break
        
    if len(line) == 0 :
        count += 1
        
print(count)
    

