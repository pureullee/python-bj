

import sys


n, m = map(int,input().split())

board = []
case = []
count1 = 0 # BWBW...
count2 = 0 # WBWB...
count_list = []
num = 0

for i in range(n) :
    row = list(sys.stdin.readline().rstrip())
    board.append(row)

for i in range(n-7) :
    for j in range(m-7) :
        case = []
        for a in range(i,i+8) :
            case.append(board[a][j:j+8])
        
        
        case_1 = []
        for k in range(8) :
            
            if k % 2 == 0 :
                
                case_1.append(case[k])
                
            if k % 2 == 1:
                case_1.append(case[k][::-1])
           
        case_1 = sum(case_1,[])
        
        while num < 63 : ## count1 ... BWBW
            
            if case_1[num] == 'W' and case_1[num+1] == 'B' :
                count1 +=2
                
            elif case_1[num] == 'B' and case_1[num+1] == 'W' :
                pass
            
            else :
                count1 +=1
            num+=2
            
        num = 0    
        while num < 63 : ## count2 ... WBWB
            
            if case_1[num] == 'B' and case_1[num+1] == "W" :
                count2 +=2
                
            elif case_1[num] == 'W' and case_1[num+1] == "B" :
                pass
            
            else :
                count2 +=1
           
            num+=2
        num = 0
        
        count_list.append(min(count1,count2))
        
        
        
        count1=0
        count2=0

print(min(count_list))
                
        
                
                
            
            
            
        
        
