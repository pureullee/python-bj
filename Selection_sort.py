import sys

n, k = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))
count = 0
j=0

while count < k :
    max_idx = 0
    if n-j == 1 : 
        print(-1)
        break
    for i in range(1,n-j):
       if data[i] > data[max_idx] :
           max_idx = i
    
    if max_idx != n-1-j :
        data[max_idx], data[n-1-j] = data[n-1-j], data[max_idx]
        count += 1
    if count == k :
        print(data[max_idx], data[n-1-count])
    
    j+=1 # while 구문이 몇바퀴 도는지 체크 
#머가 문제지..

        
    


                