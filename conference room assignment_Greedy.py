#1931

import sys


n = int(input())
data = []
answer = []
count = 0
for _ in range(n) :
    data.append(list(map(int, sys.stdin.readline().split())))
    
data.sort()

for i in range(n) :
    
    if len(answer) == 0 :
        answer.append(data[i])
        count+=1
        continue
    
    if data[i][0] < answer[0][1] and data[i][1] < answer[0][1] :
        answer[0] = data[i]
    
    elif answer[0][1] <= data[i][0] : 
        
        answer[0] = data[i]
        count+=1

print(count)
        
    
        
    
    
    
        
    
    


    