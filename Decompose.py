n = int(input())
count = 0
for i in range(1,n+1) :
    m = i
    for j in list(str(i)) :
        m+=int(j)
        
    if m == n :
        print(i)
        count = 1
        break
    
    
if count ==0 : print(0)
    
   
    
    