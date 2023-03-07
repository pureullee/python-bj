
n = int(input())


data = [[0]*10 for i in range(n+1)]
orignal = [0,1,1,1,1,1,1,1,1,1]

data[1] = orignal

i=2 
if n>=2 :
    for i in range(2, n+1) :
        
        for j in range(10) :
            if j == 0 :
                
                data[i][j] = data[i-1][j+1]
                
            elif j == 9 :
                data[i][j] = data[i-1][j-1]
                
            else :
                data[i][j] = data[i-1][j-1] + data[i-1][j+1]
               
        
                
sum = 0

for element in data[n] :
    sum += element
    
print(sum%1000000000)

    
    
    
    
    


        
        
    
      
        
            
            
            
            
    
    
    
    
            
    
            
    
    
    
    
    
    
    
        
    




            
    
    

        
         
    
    
            
            
        
        
    
    
    
    
    
    
    
        
    
    
    
    

