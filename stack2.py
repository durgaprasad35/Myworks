class Stack:
    def __init__(self):
        self.stack = [] 
    def push(self,data):
        self.stack.append(data) 
    def pop(self):
        if len(self.stack)==0:
            print("The stack is empty")
        else:
            self.stack.pop() 
    def size(self):
        return len(self.stack) 
    def is_empty(self):
        return len(self.stack)==0
    def get_stack(self):
        return self.stack    
s1 = Stack() 
s1.push(10) 
s1.push(20) 
s1.push(30)
print(s1.size()) 
print(s1.is_empty())
print(s1.get_stack()) 
s1.pop() 
print(s1.get_stack()) 
print(s1.size()) 
print(s1.is_empty())
s1.pop() 
s1.pop() 
print(s1.size()) 
print(s1.is_empty())