#20936

import sys
data =  sys.stdin.readline().strip()

op = ["+","-","*","/"]
ls = []
num =""


for s in data :
    
    
    if s not in op :
        num = num + s
        
        
    else :
        ls.append(num)
        ls.append(s)
        num =""
ls.append(num)
        

max = eval(ls[0]+ls[1]+ls[2])

        
    

