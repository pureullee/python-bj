import sys
import itertools


result = []

n, m = map(int,input().split())
str_list = list(sys.stdin.readline().split())
#print(str_list)
int_list = list(map(int, str_list))

if n == 3 :
    print(sum(int_list))

result = list(itertools.combinations((int_list),3))
result_sum = list(set(map(sum, result)))

if m in result_sum :
    print(m)
    
else :
    result_sum.append(m)
    result_sort = sorted(result_sum)
    print(result_sort[result_sort.index(m)-1])
        
    
        

    






