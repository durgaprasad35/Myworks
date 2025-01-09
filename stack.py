class Stack:
    def __init__(self):
        self.my_stack=[] 
    def is_empty(self):
        return len(self.my_stack)==0 
    def push(self,data):
        self.my_stack.append(data) 
    def pop(self):
        if not self.is_empty():
            self.my_stack.pop() 
        else:
            print("The stack is empty") 
    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]
        else:
            print("The stack is empty") 
    def size(self):
        return len(self.my_stack) 
s1 = Stack() 
s1.push(10) 
s1.push(20) 
s1.push(30) 
s1.push(40) 
print(s1.my_stack) 
print(s1.peek()) 
print(s1.is_empty()) 
print(s1.size())