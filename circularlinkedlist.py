class Node:
    def __init__(self,data):
        self.data  = data
        self.nxt = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,element,index=0):
        new_node = Node(element)
        if index<=1:
            new_node.nxt = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(1,index-1):
                if temp.nxt:
                    temp = temp.nxt
            new_node.nxt = temp.nxt
            temp.nxt = new_node
    def append(self, element):
        new_node = Node(element)
        # self.head is pointing node already
        if self.head: 
            temp = self.head
            while temp.nxt:
                temp = temp.nxt
            temp.nxt = new_node
        else: # self.head is None
            self.head = new_node
    def print_list(self):
        if self.head:
            temp = self.head
        while temp.nxt:
            print(temp.data, end = "->")
            temp = temp.nxt
        print(temp.data)
list1 = Linkedlist()

list1.append(10)
list1.append(20)
list1.append(30)
list1.insert(5)
list1.insert(6)
list1.print_list()



