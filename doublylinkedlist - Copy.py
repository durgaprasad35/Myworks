class Node:
    def __init__(self,data):
        self.data = data
        self.pre = None 
        self.nxt = None 
def insert_at_begining(head,data):
    new_node = Node(data) 
    new_node.nxt = head 
    if head:
        head.pre = new_node 
    return new_node 
def display(head):
    current = head 
    while current:
        print(current.data,end="<->") 
        current = current.nxt 
    print("None") 
def insert_after_node(node,data):
    if node is None:
        print("The node is None") 
        return 
    new_node = Node(data) 
    new_node.pre = node 
    new_node.nxt = node.nxt 
    if node.nxt:
        node.nxt.pre = new_node 
    node.nxt = new_node 
head = None
head = insert_at_begining(head,4)
head = insert_at_begining(head,3) 
head = insert_at_begining(head,2) 
head = insert_at_begining(head,1)
display(head) 
head = Node(1) 
node2 = Node(2) 
node3 = Node(3) 
head.nxt = node2 
node2.pre = head 
node2.nxt = node3 
node3.pre = node2 
display(head)
insert_after_node(node2,4) 
display(head)
    