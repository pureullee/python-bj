#1541 

import sys


s = sys.stdin.readline().rstrip().split('-')

data = []
count = 0
for i in s :
    
    if count == 0 :
        
        ans = sum(list(map(int,i.split('+'))))
        count = 1
        
    else :
        
        ans -= sum(list(map(int,i.split('+'))))
        
print(ans)
    
    
    







        

        
    
    
    

    
    
    
    
    
    



    
    
    
    
    
    
      
  
    
    
    
  
    
     
    
    