l = [] 
n = int(input("Enter length of array: ")) 
for i in range(n):
    char = int(input("Enter your characters from first to last: "))
    l.append(char) 
start = 0 
end = len(l)-1 
result = True
while(start<=end): 
    if l[start]!=l[end]:
        result= False 
    else:
        start = start+1 
        end = end-1      
    print("It is a palindrome number")
else:
    print("it is not a palindrome")
    
