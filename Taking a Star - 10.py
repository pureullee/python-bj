#2447
a = int(input())
star = [[' ' for x in range(a)]] * a
def take_star(n) : 
    
    if n == 3 :
        
        star[0] = star[2] = ['*','*','*']
        star[1] = ['*',' ','*']
        
        return
    
    take_star(n/3)
                


    
    
     
    
    
    
    
    
    
    