# def bubbleSort(arr):
#     n = len(arr) 
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j] 
# arr = list(map(int,input().split())) 
# bubbleSort(arr) 
# print(f"The sorted array is {arr}") 



def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
l = [7,5,8,1,0]
bubblesort(l)
print(l)