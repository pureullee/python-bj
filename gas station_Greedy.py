#13305

import sys


n = int(input()) #num of citys
len_list = list(map(int, sys.stdin.readline().split()))
pri_list = list(map(int, sys.stdin.readline().split()))
data = []
total_cost = 0

for x, y in zip(pri_list,len_list) :
    data.append([x,y])

cost = data[0][0] 
dis = data[0][1]
    
for i in range(1,n-1) :
    
    if data[i][0] > cost :
        dis += data[i][1]
        continue
    total_cost += cost * dis
    cost = data[i][0]
    dis = data[i][1]
total_cost += cost * dis       
print(total_cost)
    
    
        
    
    
    
    
