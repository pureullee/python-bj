#15649

n, m = map(int,input().split())

flag = [False] * (n+1) ## flag[i]가 false라면 리스트에 들어가 있지 않은 값
data = [] ## 수열 출력을 위한 리스트로, 길이가 m이 되면 출력

def func(n, m) :
    
    if len(data) == m : 
        print(" ".join(list(map(str,data))))
        return
    
    for i in range(1,n+1) :
        
        if not flag[i] :
            data.append(i)
            flag[i] = True
            func(n, m) 
            flag[i] = False
            data.pop()
        
func(n,m)
        
        
    
    

            
            
        
    
    

        
        
        
        
        
        
    
    
    
    
    

    