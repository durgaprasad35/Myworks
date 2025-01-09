class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 
def levelOrdertraversal(root):
    if root is None:
        return 
    queue = [] 
    queue.append(root) 
    while queue:
        current_node = queue.pop(0) 
        print(current_node.value) 
        if current_node.left:
            queue.append(current_node.left) 
        if current_node.right:
            queue.append(current_node.right) 
root = Node(11) 
root.left = Node(6)  
root.right = Node(15) 
root.left.left = Node(3) 
root.left.right = Node(8) 
root.left.left.left = Node(1) 
root.left.left.right = Node(5) 
root.right.left = Node(13) 
root.right.left.left = Node(12) 
root.right.left.right = Node(14) 
root.right.right = Node(17) 
root.right.right.right= Node(19) 
levelOrdertraversal(root) 
 