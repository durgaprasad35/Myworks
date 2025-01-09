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
            self._insert_rec(self.root,key) 
    def _insert_rec(self,node,key):
        if key<node.val:
            if node.left is None:
                node.left = TreeNode(key) 
            else:
                self._insert_rec(node.left,key) 
        else:
            if node.right is None:
                node.right = TreeNode(key) 
            else:
                self._insert_rec(node.right,key) 
    def search(self,key):
        return self._search_rec(self.root,key) 
    def _search_rec(self,node,key):
        if node is None or node.val == key:
            return node 
        if key<node.val:
            return self._search_rec(node.left,key) 
        return self._search_rec(node.right,key)
    def delete(self,key):
        self.root = self._delete_rec(self.root,key) 
    def _delete_rec(self,node,key):
        if node is None:
            return node 
        elif key<node.val:
            return self._delete_rec(node.left,key) 
        elif key>node.val:
            return self._delete_rec(node.right,key) 
        else:
            if node.left is None:
                return node.right 
            elif node.right is None:
                return node.left 
            min_larger_node = self._min_value_node(node.right) 
            node.val = min_larger_node.val 
            node.right = self._delete_rec(node.right,min_larger_node.val) 
        return node 
    def _min_value_node(self,node,key):
        current = node 
        while current.left is not None:
            current = current.left 
        return current 
bst = BST() 
values = [50,30,70,20,40,60,80] 
for value in values:
    bst.insert(value) 
print(bst.search(70))
