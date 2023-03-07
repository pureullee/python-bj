#11729

count = 0
data =[]
def Hanoi(size, x, y) :
    global count
    
    if size > 1 :
        Hanoi(size-1, x, 6-x-y)
        
    count +=1
    data.append([x,y])
    if size > 1 :
        Hanoi(size-1, 6-x-y, y)
        
n = int(input())

Hanoi(n,1,3)
print(count)

for i in data :
    print(i[0], i[1])
        
    
    
    
    