#1149
import sys


n = int(input())

data = [None] * n
dp =[[None] *3 for x in range(n)]
for i in range(n) :
    data[i] = list(map(int,sys.stdin.readline().split()))
    
dp[0] = data[0]

for i in range(1, n) :
    
    for j in range(3) :
        if j == 0 :
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + data[i][j]
            
        elif j == 1 :
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + data[i][j]
        
        else :
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + data[i][j]
            
print(min(dp[n-1]))

        
    

    

    



