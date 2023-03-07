#1904


data = [None] * 1000001
data[1] = 1
data[2] = 2
data[3] = 3
define = 15746



n = int(input())

for i in range(4, n+1) :
    data[i] = (data[i-1] + data[i-2]) % define
    
print(data[n])
    
     
        
    
        
    
    




    
    
    