class Node:
    def __int__(self,element):
        self.data = element
        self.nxt = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,element,index=0):
      self.element = element
      new_node = Node(element)
      if index<=1:
          new_node.nxt = self.head
          self.head = new_node
      else:
          temp = self.head
          for _ in range (1,index-1):
            if  temp.nxt:
                temp = temp.nxt
          new_node.nxt = temp.nxt
          temp.nxt  = new_node 
    def print_list(self):
        if self.head:
            temp = temp.nxt
            while temp.nxt:
                print(temp.data,end = "->")
                temp = temp.nxt
            print(temp.data)

list1 = Linkedlist()
list1.insert(10)
list1.insert(20)
list1.insert(30)
        
