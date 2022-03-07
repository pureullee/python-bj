
n = int(input())
a = int(n/10)
b = n%10
cycle_count = 0

while True :
    
    
    n_cycle = b * 10 + (a+b)%10
    
    cycle_count += 1
    
    if n_cycle == n :
        break
    
    a = int(n_cycle/10)
    b = n_cycle%10
    
print(cycle_count)
    
    
        
 