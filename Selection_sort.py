#23881
import sys 

result_list = []

n, k = map(int,input().split())
data = list(map(int, sys.stdin.readline().split()))
count = 0
while True :
    Max = max(data[0:n-count])
    i = data.index(Max)
    if data[-1-count] != Max :
        data[i] = data[-1-count]
        data[-1-count] = Max
        result_list.append([data[i],Max])
    count += 1
    if count >= n-1 : break

if len(result_list) < k :
    print(-1)
else :
    print(result_list[k-1][0], result_list[k-1][1])
    


                