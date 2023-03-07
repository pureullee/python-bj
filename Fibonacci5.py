#10870

def fibo(a) :
    if a == 0 :
        return 0
    
    if a == 1 :
        return 1
    
    return fibo(a-2)+fibo(a-1)

print(fibo(10))
