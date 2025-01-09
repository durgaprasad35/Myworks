class Queue:
    def __init__(self):
        self.Queue = [] 
    def push(self,data):
        self.Queue.append(data) 
    def pop(self):
        if len(self.Queue)==0:
            print("The Queue is empty") 
        else:
            self.Queue.pop(0) 
    def size(self):
        return len(self.Queue) 
    def is_empty(self):
        return len(self.Queue)==0 
    def get_Queue(self):
        return self.Queue 
q = Queue()
q.push(10) 
q.push(20) 
q.push(30) 
print(q.size() )
print(q.is_empty()) 
print(q.get_Queue()) 
q.pop() 
q.pop() 
print(q.size() )
print(q.is_empty() )
print(q.get_Queue()) 
q.pop()
print(q.size() )
print(q.is_empty() )
print(q.get_Queue())

