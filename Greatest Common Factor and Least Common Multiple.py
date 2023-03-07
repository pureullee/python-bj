#2609

a, b = map(int,input().split())

if a >= b :
    large = a
    min = b
else : 
    large = b
    min = a
    
for i in range(1,min+1) :
    
    if min % i == 0 and large % i == 0 :
        fac = i 
n = 1
while True :
    
    if (min * n) % large == 0 :
        break
    n += 1
    
print(fac)
print(min* n) 
    