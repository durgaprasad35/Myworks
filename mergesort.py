def mergeSort(arr):
    if len(arr)>1:
        r = len(arr)//2
        l = arr[:r] 
        m = arr[r:] 
        mergeSort(l) 
        mergeSort(m) 
        i=j=k=0 
        while i<len(l) and j<len(m):
            if l[i]<m[j]:
                arr[k]=l[i] 
                i+=1 
            else:
                arr[k] = m[j] 
                j+=1 
            k+=1 
        while i<len(l):
            arr[k] = l[i] 
            i+=1
            k+=1 
        while j<len(m):
            arr[k]=m[j] 
            j+=1
            k+=1 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ") 
arr = [1,789,0,3] 
mergeSort(arr) 
printList(arr)



