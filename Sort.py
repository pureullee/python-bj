

def Sort(data) :
    
    for i in range(len(data)-1) :
        swap = False
        
        for j in range(len(data)-i-1) :
            if data[j]>data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if swap == False :
            break
    
    return data


if __name__ == "__main__" :
    
    n = int(input())
    
    data = []
    
    for i in range(n):
        data.append(int(input()))
        
    Sort(data)
    
    for i in data :
        print(i,end = '')

        
        
    
    
    




