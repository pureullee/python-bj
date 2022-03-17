
size_list=[]
rank = 1

n = int(input())

for i in range(n) :
    a, b = map(int,input().split())
    size_list.append([a,b])
    
for i in range(n) :
    
    for j in range(n):
        
        if size_list[i][0] < size_list[j][0] and size_list[i][1] < size_list[j][1] :
            rank+=1
            
    
    
    print(rank, end=' ')
    rank = 1
    
    
    
    




        
        

        
    


        
        
        
            
        
    

    
   

    
