class Node:
    def __init__(self,data):
        self.data = data 
        self.nxt = None 
def insert_at_begining(head,data):
    new_node = Node(data) 
    new_node.nxt = head 
    return new_node 
def insert_after_node(node,data):
    if node is None:
        print("Error:There is no nodes are present (None)") 
        return 
    new_node = Node(data) 
    new_node.nxt = node.nxt 
    node.nxt = new_node 
def insert_at_end(head,data):
    new_node=Node(data) 
    if head is None:
        return new_node 
    current = head 
    while current.nxt:
        current = current.nxt 
    current.nxt = new_node 
    return head 
def Traverse(head):
    current = head 
    while current:
        print(str(current.data)+"->",end=" ") 
        current = current.nxt 
    print("None") 
head = None 
head = insert_at_begining(head,4) 
head = insert_at_begining(head,3) 
head = insert_at_begining(head,2) 
head = insert_at_end(head,5) 
Traverse(head) 
