import sys

a = 0

str_list = list(sys.stdin.readline().rstrip())
to_num = list(map(ord,str_list)) 

for i in to_num :
    if i < 80 :
        a += int((i-65)/3) + 2
    elif i < 84 :
        a += 7
    elif i < 87 :
        a += 8 
    elif i < 91 :
        a += 9
        
print(a+len(to_num))









    
    