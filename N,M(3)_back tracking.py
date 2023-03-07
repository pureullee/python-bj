#15651

n, m = map(int, input().split())

data =[]

def func(n,m) :
    
    if len(data) == m :
        print(" ".join(list(map(str,data))))
        return
    
    for i in range(1, n+1) :
        data.append(i)
        func(n,m)
        data.pop()
        
func(n,m)    