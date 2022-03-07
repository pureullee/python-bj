
n = int(input())

if n <= 99 :
    print(n)
    
else :
    count = 99
    
    for i in range(100, n+1) :
        a = int(i/100)
        b = int((i%100) / 10)
        c = int(i%10)
        
        if a - b == b - c :
            count += 1
    
    print(count)
        