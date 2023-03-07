#11659

import sys


n, m = map(int,input().split())
data = list(map(int,sys.stdin.readline().split()))
dp = [0] * 100001
dp[1] = data[0]
for i in range(2, n+1) :
    dp[i] = dp[i-1] + data[i-1]

    
for i in range(m) :
    a, b = map(int,input().split())
    ans = dp[b] - dp[a-1] 
    print(ans)
    
    
    
        
    
   
        
        
        
    
    
    
        
        
    
    
    

