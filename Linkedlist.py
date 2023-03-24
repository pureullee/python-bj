'''class Node :
    
    def __init__(self, value, next:'Node'=None) :
        self.value = value
        self.next = next
        
class linkedList :
    ncount = 0
    
    def __init__(self, n :'Node') :
        if self.ncount == 0 :
            self.__head__ =  Node('dummy', None)
            
    
        self.n = n
        self.__head__.next = self.n
        self.ncount +=1
        self.perv = self.__head__
        
    def print(self) :
        
        while True :
            print(self.perv.next.value)
            self.perv = self.perv.next
            if self.perv.next == None : break
            
    def append(self, value) :
        
        while self.perv.next != None :
            self.perv = self.perv.next
        self.perv.next = Node(value, None)'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = Node('dummy')
        self.tail = self.head
        self.count = 0

    def print(self):
        current_node = self.head.next
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1
        
        
    def insert(self,value,inx) :
        perv_node = self.head
        self.ptr = 1
        if inx <= self.count :
            while self.ptr != inx :
                perv_node = perv_node.next
                self.ptr += 1
            new_node = Node(value,perv_node.next)
            perv_node.next = new_node
            self.count +=1
            
    def pop(self) :
        perv_node = self.head
        self.ptr = 1 
        while self.ptr != self.count :
            perv_node = perv_node.next
            self.ptr +=1
            
        result = perv_node.next
        perv_node.next = None
        self.tail = perv_node
        self.count -= 1
        return result.value
            
   
            
        
        
        
        
ls = LinkedList()
ls.append(3)
ls.append(5)
ls.insert(2,1)
print(ls.pop())
ls.append(7)
ls.print()

        
        
        
        
        
        
        
        
            
            
        
        
            
        
        
            


        
        
        