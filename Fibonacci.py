

        

call_list = [[1,0],[0,1]] #리스트 내의 투플 형태 


def fibonacci(t) :
    
    if len(call_list)-1 < t :
        size = len(call_list) -1
        
        while size < t :
            
            call_list.append([x+y for x,y in zip(call_list[size],call_list[size-1])])
            size += 1
            
    print(call_list[t][0], call_list[t][1])
            
n= int(input())

for i in range(n) :
    fibonacci(int(input()))        
            
            
            

    
    
    

    
