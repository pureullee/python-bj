#9461

data = [None] * 101
data[1:11] = [1,1,1,2,2,3,4,5,7,9]

def func(n) :
    
    if data[n] :
        result = data[n]
    else :
        result = func(n-1) + func(n-5)
        data[n] = result
    return result

t = int(input())

for i in range(t) :
    print(func(int(input())))


    
