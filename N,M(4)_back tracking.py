#15652

n, m = map(int, input().split())

data =[]

def func(j,n,m) :
    
    if len(data) == m :
        print(" ".join(list(map(str,data))))
        return
    
    for i in range(j, n+1) :
        data.append(i)
        func(i,n,m)
        data.pop()
        
func(1,n,m)    