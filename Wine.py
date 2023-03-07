#2156
import sys


n = int(input())
data = []
for i in range(n) :
    data.append(int(sys.stdin.readline()))
    

dp = [0] * (n+3)

dp[0] = 0
dp[1] = data[0]
if n>=2 :
    dp[2] = data[0] + data[1]

if n>=3 :
    for i in range(3,n+1) :
        dp[i] = max(dp[i-2] + data[i-1], dp[i-3] + data[i-2] + data[i-1], dp[i-1])
    
print(max(dp))
    




    



        
        
        
        
        
    
        
        
        
    
    
    
    
    
    
    
    
    
    