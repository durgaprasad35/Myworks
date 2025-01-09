stack = [] 
def text_editor(text):
    stack.append(text) 
def backspace(back):
    if len(stack)!=0:
        if back == "<":
            stack.pop()
        else:
            print("Press correct button to backspace") 
    else:
        print("There is no text")
text = input() 
back = input() 
text_editor(text) 
print(stack) 
backspace(back)
 
