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
        while current_node != self.head:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value,self.head)
        self.tail.next = new_node
        self.tail_pre = self.tail # tail 바로 이전의 노드 
        self.tail = new_node
        self.count += 1
        
        
    def insert(self,value,inx) :
        perv_node = self.head
        self.ptr = 0
        if inx <= self.count-1 :
            while self.ptr != inx :
                perv_node = perv_node.next
                self.ptr += 1
            new_node = Node(value,perv_node.next)
            perv_node.next = new_node
            if inx == self.count -1 : #tail 바로 이전의 삽입 경우엔 tail_pre를 갱신해줘야함
                self.tail_pre = new_node
            self.count +=1
            
    def pop(self) : #이경우엔 항상 o(n)의 복잡도를 가져 비효율적
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
    
    def pop_new(self) :
        
        perv_node = self.tail_pre
        result = self.tail.value
        perv_node.next = self.head 
        self.tail = perv_node 
        self.count -=1
        return result
    
    def reverse(self) :
        if self.count >= 2 :
            perv_node = self.head
            curr_node = self.head.next
            next_node = curr_node.next
            
            self.tail = curr_node ## 첫번째 노드가 끝이 될 것이기에
            self.tail_pre = next_node#2번째 노드가 테일 이전노드가 될것이기에 
        
        
            for i in range(self.count +1 ) :
                curr_node.next = perv_node #현재 노드의 다음노드가 이전 노드 
            
                perv_node = curr_node #이전 노드를 현재 노드로 만들어줌
                curr_node = next_node # 현재 노드를 3줄에서 저장한 현재 노드로 다시 만들어줌... 이까지 과정을 거쳐 0 1 2 -> 1 2
                next_node = curr_node.next #이로 인해 다시 3에 저장된 노드를 일단 넥스트로 만들어줌.
                
            
            
        
            
            
       
        
        
        
        
        
        
            
   
            
        
        
        
        
ls = LinkedList()
ls.append(3)
ls.append(5)
ls.insert(2,1)
ls.print()

ls.reverse()
ls.print()
print("ㄱ부ㅜㄴ")
ls.append(6)
ls.print()



        
        
        
        
        
        
        
        
            
            
        
        
            
        
        
            


        
        
        