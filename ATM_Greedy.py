#11399
import sys


n = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

for i in range(1,n) :
    data[i] = data[i-1] + data[i]
    
print(sum(data))


