
data = [None] * 1000001

         
n = int(input())

data[1] = 0
data[2] = 1
data[3] = 1

for i in range(4, n+1) :
    
    result = data[i-1] + 1
        
    if i%3 == 0 :
        if result > data[i//3] +1 :
            result = data[i//3] +1
        
    if i%2 == 0 :
        if result > data[i//2] + 1 :
            result = data[i//2] + 1
                
    data[i] = result
        
print(data[n])

