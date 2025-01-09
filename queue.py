class Queue:
    def __init__(self):
        self.my_queue = [] 
    def is_empty(self):
        return len(self.my_queue)==0 
    def enqueue(self,data):
        return self.my_queue.append(data) 
    def deQueue(self):
        if len(self.my_queue)!=0:
            return self.my_queue.pop(0) 
        else:
            print("The Queue is empty") 
    def peek(self):
        if len(self.my_queue)!=0:
            return self.my_queue[-1] 
        else:
            print("The Queue is empty") 
    def size(self):
        return len(self.my_queue) 

q1 = Queue() 
q1.enqueue(10) 
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40) 
print(q1.my_queue) 
print(q1.peek()) 
print(q1.size()) 
print(q1.is_empty()) 
q1.deQueue() 
q1.deQueue() 
print(q1.my_queue) 
