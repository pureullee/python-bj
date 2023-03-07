#11047

import sys


n, k = map(int,input().split())
count = 0
coin_list = []

for i in range(n) :
    coin_list.append(int(input()))
    
for i in reversed(range(n)) :
    
    if k //coin_list[i] == 0 :
        pass
    else :
        count += k // coin_list[i]
        
        k = k % coin_list[i]
        

print(count)  
    
    





            

    
        
        