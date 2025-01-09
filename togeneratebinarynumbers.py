def binaryNumbers(arr):
    n = len(arr) 
    arr.append(1) 
    for i in range(n):
        current = str(arr.pop(0)) 
        n1 = current+"0" 
        n2 = current+"1" 
        arr.append(n1) 
        arr.append(n2) 
    return arr 
arr = [] 
result = binaryNumbers(arr) 
print(result)