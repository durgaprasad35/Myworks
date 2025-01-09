class TreeNode:
    def __init__(self,key):
        self.left = None 
        self.right = None 
        self.val = key 
class BST:
    def __init__(self):
        self.root = None 
    def insert(self,key):
        if self.root is None:
            self.root = TreeNode(key) 
        else:
            self._insert_rc(self.root,key) 
    def _insert_rc(self,node,key):
        if key<node.val:
            if node.left is None:
                node.left = TreeNode(key) 
            else:
                self._insert_rc(node.left,key) 
        else:
            if node.right is None:
                node.right =TreeNode(key) 
            else:
                self._insert_rc(node.right,key) 
    def preorder_Traversal(self,node,key):
        if node:
            print("node: ",node.val) 
            self.preorder_Traversal(node.left) 
            self.preorder_Traversal(node.right) 
    def inorder_Traversal(self,node,key):
        if node:
            self.inorder_Traversal(node.left) 
            print("node: ",node.val) 
            self.inorder_Traversal(node.right) 
    def Postorder_Traversal(self,node,key):
        self.postorder_Traversal(node.left)
        self.postorder_Traversal(node.right) 
        print("node: ",node.val) 
bst = BST() 
values = [50,70,30,20,60,80] 
for i in values:
    bst.insert(i)  
print(bst.preorder_Traversal()) 
print(bst.inorder_Traversal()) 
print(bst.Postorder_Traversal())

 