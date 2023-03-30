#2447


def star(size) :
    if size == 3 :
        s = ["***","* *","***"] 
        return s
    else :
        new_size = size // 3
        
        top = [x*3 for x in star(new_size)] #[0]부터 [n] 까지 각 요소에 3배
        middle = [x + " " * new_size + x for x in star(new_size)] #각 요소에 star, 공백, star로 
        bottom = top[:] #bottom은 top이랑 같은구조
        
        return top + middle + bottom
                  
    
    
    
size = int(input())
print("\n".join(star(size)))

        
        


