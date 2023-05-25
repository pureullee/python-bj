

class Node :
    def __init__(self, item) -> None:
        self.item = item
        self.left = None
        self.right = None
        
class BinarySearchTree : 
    def __init__(self) :
        self.__root = None
        
        
    def insert(self, item) :
        self.__root = self.__insertItem(self.__root,item)
        
        
        
    
    def delete(self, item) :
        self.__root = self.__deleteItem(self.__root, item)
    
    def search(self, item) :
        return self.__searchItem(self.__root, item)
    
    def __searchItem(self, n : 'Node', item) :
        
        #검색 실패
        if n == None :
            return None
        
        #검색 성공
        elif n.item == item :
            return n
        
        
        
        #주목 노드의 값 보다 검색 값이 큰 경우
        elif n.item < item :
            return self.__searchItem(n.right, item)
        
        #주목 노드의 값 보다 검색 값이 작은 경우
        else :
            return self.__searchItem(n.left, item)
    
    def __insertItem(self, n: 'Node', item) :
        
        #삽입 성공 
        if n == None :
            n = Node(item)
            
        #삽입 실패
        elif n.item == item :
            return None
        #주목 노드의 값 보다 삽입 값이 큰 경우   
        elif n.item < item :
            n.right=self.__insertItem(n.right, item)
        #주목 노드의 값 보다 삽입 값이 작은 경우
        else :
            n.left= self.__insertItem(n.left, item)
        return n
        
    
        
    def pre_order_traverse(self) :
        
        self.__pre(self.__root)
    
    def __pre(self, n : 'Node') :
        if n != None :
            print(n.item, end=' ')
            self.__pre(n.left)
            self.__pre(n.right)

    def in_order_traverse(self) :
        print('')
        self.__ord(self.__root)
        
    def __ord(self, n:'Node') :
        if n!= None :
            self.__ord(n.left)
            print(n.item, end=' ')
            self.__ord(n.right)
    
        
        
    
    
        
        
            
            
bst1 = BinarySearchTree()

bst1.insert(55)

bst1.insert(15)

bst1.insert(60)

bst1.insert(8)

bst1.insert(28)

bst1.insert(90)

bst1.insert(3)

bst1.insert(18)

bst1.insert(45)

bst1.insert(41)

bst1.insert(48)

bst1.insert(30)

bst1.insert(50)

bst1.insert(38)

bst1.insert(33)

bst1.insert(32)

bst1.insert(36)

bst1.pre_order_traverse()       # 결과를 도식화 할 것

bst1.delete(28)

bst1.in_order_traverse()         # 결과를 도식화 할 것

#bst1.delete(30)

#bst1.post_order_traverse()    # 결과를 도식화 할 것              
        
                
            
            
        
        
    
    
        
        