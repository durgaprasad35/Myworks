class Stack:
    def __init__ (self):
        self.stack=[]
    def pop(self):
        if len(self.stack)<1:
            return None
        return self.stack.pop()
    def push(self,item):
        return self.stack.append(item)
    def size(self):
        return len(self.stack)


s=Stack()
s.push(1)
s.push(2)
s.push(3)

print(s)
print(s.pop)
    



