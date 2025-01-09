stack = [] 
reverse_stack = []
def push(data):
    stack.append(data) 
def pop():
    if len(stack)!=0:
        stack.pop() 
    else:
        print("The stack is empty") 
push("1") 
push("2") 
push("2") 
# push("a") 
# push("m")  
original = " ".join(stack) 
for i in range(len(stack)):
    j = stack.pop() 
    reverse_stack.append(j)  
reverse = " ".join(reverse_stack) 
if original == reverse:
    print("Palindrome string") 
else:
    print("Not a palindrome string") 
