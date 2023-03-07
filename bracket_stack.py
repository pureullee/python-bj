#9012
import sys




n = int(input())

for x in range(n) :
    stk = []
    com = list(sys.stdin.readline().rstrip())
    t = 0
    for k in com :
        
        if k == '(' :
            stk.append(k)
            
        else :
            if len(stk) == 0 :
                print("NO")
                t = 1
                break
            
            else :
                stk.pop()
                
        
    if len(stk) == 0 and t == 0 :
        print("YES")
    
    if len(stk) != 0 :
        print("NO")
        
            
            


