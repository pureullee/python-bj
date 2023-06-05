

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
        self.__root = self.__delete(self.__root,item)
    
    #삭제 노드 찾기  
    def __delete(self, n:'Node', item) :
    
        if n == None :
            return None
        elif n.item == item :
            n = self.__deleteNode(n)
        elif n.item < item :
            n.right = self.__delete(n.right, item)
        else :
            n.left = self.__delete(n.left, item)
        return n
        
    def __deleteNode(self, n:'Node') :
        
        #자식이 없는 경우
        if n.left == None and n.right == None :
            return None 
        
        # 자식이 2개인 경우    
        elif n.left and n.right :
            # 오른 자식중에 가장 작은 값을 찾기 위함
            (rtnItem, rtnNode) = self.__deleteM(n.right)
            n.item = rtnItem
            n.right = rtnNode
            return n
            
        # 왼자식만
        elif n.left :
            return n.left
            
        # 오른 자식만
        elif n.right:
            return n.right
    
    def __deleteM(self, n:'Node'):
        
        # 왼자식이 없는 경우에 지금 값과, 오른 자식들을 리턴 
        if n.left == None :
            return (n.item, n.right)
        # 아니라면 왼자식 없는 경우를 찾으러 
        else :
            (rtnItem, rtnNode) = self.__deleteM(n.left)
            n.left = rtnNode
            
            return (rtnItem, n)
            
    
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
        
    
    
    #전위순회    
    def pre_order_traverse(self) :
        
        self.__pre(self.__root)
    
    def __pre(self, n : 'Node') :
        if n != None :
            print(n.item, end=' ')
            self.__pre(n.left)
            self.__pre(n.right)

    #중위 순회
    def in_order_traverse(self) :
        print('')
        self.__ord(self.__root)
        
    def __ord(self, n:'Node') :
        if n!= None :
            self.__ord(n.left)
            print(n.item, end=' ')
            self.__ord(n.right)
    
    #후위 순회
    
    def post_order_traverse(self) :
        print('')
        self.__post(self.__root)
    def __post(self, n:'Node') :
        if n!= None :
            self.__post(n.left)
            self.__post(n.right)
            print(n.item, end=' ')
        
        
class AVLNode :
    def __init__(self, item, left, right, height) :
        self.item = item
        self.left = left
        self.right = right
        self.height = height
class AVLTree :
    def __init__(self) -> None:
        self.NIL = AVLNode(None, None, None, 0)
        self.__root = self.NIL
        self.LL = 1 ; self.LR = 2 ; self.RR = 3 ; self.RL = 4
        self.NO_NEED = 0
        self.ILLEGAL = -1
        
    def __leftRotate(self, n :'AVLNode' ) :
        #기준 노드의 오른 쪽 주목 
        Rchild = n.right 
        
        # 오른 쪽 노드의 왼쪽 노드
        RLchild = Rchild.left
        
        #기준 노드를 오른 쪽 노드의 왼자식으로 
        Rchild.left = n
        #자식이 된 노드의 오른 자식은 아까 왼자식 이었던 것
        n.right = RLchild
        #높이 설정
        n.height = 1 + max(n.left.height, n.right.height)
        Rchild.height = 1 + max(Rchild.left.height, Rchild.right.height)
        return Rchild 
    
    def __rightRotate(self, n:'AVLNode') :
        
        Lchild = n.left
        
        LRchild = Lchild.right
        
        Lchild.right = n
        
        n.left = LRchild
        
        n.height = 1 + max(n.left.height, n.right.height)
        Lchild.height = 1 + max(Lchild.left.height, Lchild.right.height)
        return Lchild 
    
    def insert(self, item) :
        self.__root = self.__insertItem(self.__root, item)
        
    def __insertItem(self,n : 'AVLNode' ,item) :
        if n == self.NIL :
            n = AVLNode(item, self.NIL, self.NIL, 1)
        elif item < n.item :
            n.left = self.__insertItem(n.left, item)
            n.height = 1 + max(n.left.height, n.right.height)
            type = self.__needBalance(n)
            if type != self.NO_NEED :
                n = self.__balanceAVL(n, type) 
                
        else :
            n.right = self.__insertItem(n.right, item)
            n.height = 1 + max(n.left.height, n.right.height)
            type = self.__needBalance(n)
            if type != self.NO_NEED :
                n = self.__balanceAVL(n, type) 
        return n
    

    def __needBalance(self, n : 'AVLNode') :
        type = self.ILLEGAL
        #R 유형 
        if n.left.height +2 <= n.right.height :
            #RR
            if n.right.left.height <= n.right.right.height :
                type = self.RR
            else :
                type = self.RL
        #L 유형     
        elif n.left.height >= n.right.height + 2 :
            
            if n.left.left.height >= n.left.right.height :
                type = self.LL
            else :
                type = self.LR
        else :
            type = self.NO_NEED
        return type
    
    def __balanceAVL(self, n: 'AVLNode', type:int ) :
        rtnNode = self.NIL
        if type == self.LL :
            rtnNode = self.__rightRotate(n)
        elif type == self.LR :
            n.left = self.__leftRotate(n.left) 
            rtnNode = self.__rightRotate(n)
        elif type == self.RR :
            rtnNode = self.__leftRotate(n)
        elif type == self.RL :
            n.right = self.__rightRotate(n.right)
            rtnNode = self.__leftRotate(n)
        
        return rtnNode
    
    def search(self, item) :
        return self.__searchItem(self.__root, item)
    
    def __searchItem(self, n : 'AVLNode', item) :
        if n == self.NIL :
            return self.NIL
        
        elif item == n.item : 
            return n
        
        elif item < n.item : 
            return self.__searchItem(n.left, item)
        
        else :
            return self.__searchItem(n.right, item)
        
    def delete(self, item) :
        self.__root = self.__deleteItem(self.__root, item)
        
    def __deleteItem(self, n: 'AVLNode', item) :
        if n == self.NIL :
            return self.NIL
        
        else :
            if item == n.item : 
                n = self.__deleteNode(n)
                
            elif item < n.item :
                n.left = self.__deleteItem(n.left, item)
                n.height = 1 + max(n.left.height,n.right.height)
                type = self.__needBalance(n)
                if type != self.NO_NEED :
                    n = self.__balanceAVL(n, type)
            else :
                n.right = self.__deleteItem(n.right, item)
                n.height = 1 + max(n.left.height,n.right.height)
                type = self.__needBalance(n)
                if type != self.NO_NEED :
                    n = self.__balanceAVL(n, type)
            return n 
        
    def __deleteNode(self, n:'AVLNode') :
        
        # 0개의 자식
        if n.left == self.NIL and n.right == self.NIL :
            return self.NIL
        
        elif n.left and n.right :
            (rtnItem, rtnNode) = self.__deleteM(n.right)
            n.item = rtnItem
            n.right =rtnNode
            n.height = 1 + max(n.left.height,n.right.height)
            type = self.__needBalance(n)
            if type != self.NO_NEED :
                n = self.__balanceAVL(n, type)
            return n
        
        elif n.left :
            return n.left
        
        elif n.right :
            return n.right 
        
    
    def __deleteM(self, n:'AVLNode') :
        if n.left == self.NIL :
            return (n.item, n.right)
        
        else :
            (rtnItem, rtnNode) = self.__deleteM(n.left)
            n.left = rtnNode
            n.height = 1 + max(n.left.height,n.right.height)                   
            type = self.__needBalance(n)
            if type != self.NO_NEED :
                n = self.__balanceAVL(n, type)
            return (rtnItem, n)
        
    #전위순회    
    def pre_order_traverse(self) :
        print('')
        self.__pre(self.__root)
    
    def __pre(self, n : 'Node') :
        if n != None :
            print(n.item, end=' ')
            self.__pre(n.left)
            self.__pre(n.right)

    #중위 순회
    def in_order_traverse(self) :
        print('')
        self.__ord(self.__root)
        
    def __ord(self, n:'Node') :
        if n!= None :
            self.__ord(n.left)
            print(n.item, end=' ')
            self.__ord(n.right)
    
    #후위 순회
    
    def post_order_traverse(self) :
        print('')
        self.__post(self.__root)
    def __post(self, n:'Node') :
        if n!= None :
            self.__post(n.left)
            self.__post(n.right)
            print(n.item, end=' ')
                          
def runBST() :           
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

    bst1.delete(30)

    bst1.post_order_traverse()    # 결과를 도식화 할 것              
        
                
            
            
def runAVL() :        
    bst1 = AVLTree()

    bst1.insert(10)

    bst1.insert(20)

    bst1.insert(5)

    bst1.insert(80)

    bst1.insert(90)

    bst1.insert(7550)

    bst1.pre_order_traverse()     # 결과를 도식화 할 것

    bst1.insert(30)

    bst1.insert(77)

    bst1.insert(15)

    bst1.in_order_traverse()       # 결과를 도식화 할 것

    bst1.insert(40)

    bst1.delete(7550)

    bst1.delete(10)

    bst1.post_order_traverse()   # 결과를 도식화 할 것

    bst1.delete(5)

    bst1.pre_order_traverse()    # 결과를 도식화 할 것        
    
    
runBST()
print('\n')        
runAVL()       