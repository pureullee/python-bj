#1912

import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

dp[0] = data[0]

for i in range(1, n) :
    
    if dp[i-1] >= 0 :
        dp[i] = dp[i-1] + data[i]
    else :
        dp[i] = data[i]
        
print(max(dp))
            
        
        



        


            
            
            
        
    
    
        
    
    

                
        


