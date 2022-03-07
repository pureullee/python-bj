def d(n) :
    hap = 0
    numbers = list(map(int,list(str(n))))
    for i in numbers :
        hap += i
    return hap + n


s = set([i for i in range(1,10001)])

for i in range(1,10001) :
    if d(i) in s :
        s.remove(d(i))
        
print("\n".join(map(str, s)))
    
    
    