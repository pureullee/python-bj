#4949


import sys 

while True :
    s = sys.stdin.readline().rstrip()
    stk = [None]
    if s == '.' : break
    s = list(s)
    
    for x in s :
        
        if x == '(' or x == '[' :
            stk.append(x)
        
        elif x == ')' :
            if stk[-1] == '(' :
                stk.pop()
            else : 
                print('no')
                break
        elif x == ']' :
            if stk[-1] == '[' :
                stk.pop()
            else :
                print('no')
                break
        elif x == '.' :
            if stk[-1] != None :
                print('no') 
            else : print('yes')
            
    
    
    
    
