#10828
import sys


class sta :
    
    def __init__(self, x) :
        self.stk = [None] * x
        self.ptr = 0
        self.top = x-1
        
    def push(self, x) :
        
        self.stk[self.ptr] = x
        self.ptr += 1
        
    def pop(self) :
        
        if self.ptr == 0 :
            print(-1)
        
        else :
            self.ptr -= 1
            print(self.stk[self.ptr])
    
    def size(self) :
        print(self.ptr)
        
    def empty(self) :
        if self.ptr == 0 :
            print(1)
        else : print(0)
        
    def Top(self) :
        if self.ptr == 0 :
            print(-1)
        else :
            print(self.stk[self.ptr-1])
            
n = int(input())
s = sta(n)

for x in range(n) :
    
    command = sys.stdin.readline().split()
    
    if command[0] == "push" :
        s.push(int(command[1]))
        
    elif command[0] == "pop" :
        s.pop()
        
    elif command[0] == "size" :
        s.size()
        
    elif command[0] == "empty" :
        s.empty()
    
    elif command[0] == "top" :
        s.Top()
        
        
        