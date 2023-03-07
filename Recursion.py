##9184
data = {(1,1,1) : 2 , (2,2,2):4}

def w(a,b,c) :
    if (a,b,c) in data :
        return data[(a,b,c)]
    
    if a<=0 or b<=0 or c<=0 : 
        return 1
    
    elif a>20 or b>20 or c>20 :
        return w(20,20,20)
    elif a<b and b<c :
        
        res= w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        data[(a,b,c)] = res
        return res
    else :
        res = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) -w(a-1,b-1,c-1)
        data[(a,b,c)] = res
        return res

while True :    
    a,b,c = map(int,input().split())
    if (a,b,c) == (-1,-1,-1) : break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
    


    
    
    