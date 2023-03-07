#18258
import sys


class Queue :
    
    def __init__(self, size) :
        
        self.que = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
    def Push(self, x) :
        
        if self.front != (self.rear+1) % self.size :
            self.rear = (self.rear+1) % self.size 
            self.que[self.rear] = x
            
    def Pop(self) :
        
        if self.front != self.rear :
            
            self.front = (self.front+1) % self.size
            print(self.que[self.front])
            
        else :
            print(-1)
            
    def Size(self) :
        
        if self.rear >= self.front :
            print(self.rear - self.front)
        
        else :
            print(self.size - self.front + self.rear)
            
    def Empty(self) :
        
        if self.front == self.rear :
            print(1)
            
        else :
            print(0)
            
            
    def Front(self) :
        
        if self.front == self.rear :
            print(-1)
            
        else :
            print(self.que[(self.front+1)% self.size])
            
    def Back(self) :
        
        if self.front == self.rear :
            print(-1)
            
        else :
            print(self.que[self.rear])
            

if __name__ == "__main__" :
    
    n = int(input())
    que = Queue(n)
    for i in range(n) :
        
        com = list(sys.stdin.readline().split())
        
        if com[0] == "push" :
            
            que.Push(int(com[1]))
            
        elif com[0] == "pop" :
            
            que.Pop()
        
        elif com[0] == "size" :
            
            que.Size()
        
        elif com[0] == "empty" :
            
            que.Empty()
        
        elif com[0] == "front" :
            
            que.Front()
            
        elif com[0] == "back" :
            
            que.Back()
            
            
        
            
        
            
            
            
            
                
        
                
                
            
            
        
        