#10815
import sys


n = int(input())

data = list(set(map(int, sys.stdin.readline().split())))
data.sort()

def bin_search(x) :
    
    pl = 0
    pr = len(data) - 1
    pc = (pl+pr) // 2
    
    while True :
        
        if data[pc] == x :
            return 1
        
        elif data[pc] > x :
            pr = pc - 1
            pc = (pl+pr) // 2
        
        else :
            pl = pc + 1
            pc = (pl+pr) // 2
            
        if pl > pr : 
            return 0

m = int(input())

pro = list(map(int, sys.stdin.readline().split()))

for k in pro :
    print(bin_search(k), end=' ')


