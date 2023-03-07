import sys


result_list = []

def selection_sort(a_list, n) :
    
    Max = a_list[0] 
    j=n-1
    for i in range(0, n) :
                
        if Max < a_list[i] :
            Max = a_list[i] 
            j = i
        
        
            
    if Max != a_list[n-1] :
        if j != n-1 :
            a_list[j] = a_list[n-1]
            a_list[n-1] = Max
            result_list.append([a_list[j], Max])
        else :
            a_list[0] = a_list[n-1]      
            a_list[n-1] = Max
            result_list.append([a_list[0], Max])
        
    if n > 1 :            
        selection_sort(a_list, n-1)
                

n, k = map(int,input().split())
data = list(map(int, sys.stdin.readline().split()))   

selection_sort(data, n)

if len(result_list) < k :
    print(-1)
else :
    print(result_list[k-1][0], result_list[k-1][1])
    

                