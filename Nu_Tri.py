# 1932

import sys


n = int(input())

data =[None] * n
dp = [[None] *(x+1) for x in range(n)]
for i in range(n) :
    data[i] = list(map(int, sys.stdin.readline().split()))
    
dp[0] = data[0]

for i in range(1, n) :
    
    for j in range(i+1) :
        
        if j == 0 :
            dp[i][j] = dp[i-1][0] + data[i][j]
            
        elif j == i :
            dp[i][j] = dp[i-1][i-1] + data[i][j] 
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]
            
print(max(dp[n-1]))
        
    