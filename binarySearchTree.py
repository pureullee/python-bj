#5639
import sys
sys.setrecursionlimit(100000)
class Node :
    def __init__(self, key, parent :'Node' = None, left :'Node' = None, right:'Node'= None) :
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        

class BinaryTree :
    def __init__(self) :
        self.root = None
        
    def append(self, node:'Node') :
        if self.root == None : 
            self.root = node 
            
        else :
            new_node = node
            curr_node = self.root
            
            while True :
                if new_node.key < curr_node.key :
                    if curr_node.left == None :
                        curr_node.left = new_node
                        new_node.parent = curr_node 
                        return True
                        
                    else :
                        curr_node = curr_node.left
                        
                elif new_node.key > curr_node.key :
                    if curr_node.right == None :
                        curr_node.right = new_node
                        new_node.parent = curr_node 
                        return True
                        
                    else :
                        curr_node = curr_node.right
                        
                        

    def postorder_traversal(self, root:'Node'):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key)
            

b = BinaryTree()           
root = int(input()) 
s = Node(root)
b.append(s)
while True :
    try:
        n =int(input())
        b.append(Node(n))
    except :
        break
    
b.postorder_traversal(s)   
