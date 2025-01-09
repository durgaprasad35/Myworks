class MinHeap:
    def __init__(self):
        self.heap = [] 
    def get_parent_index(self,index):
        return (index-1)//2 
    def get_left_child_index(self,index):
        return 2*index+1 
    def get_right_child_index(self,index):
        return 2*index+2 
    def has_parent(self,index):
        return self.get_parent_index(index)>=0 
    def has_left_child(self,index):
        return self.get_left_child_index(index)<len(self.heap) 
    def has_right_child(self,index):
        return self.get_right_child_index(index)<len(self.heap) 
    def parent(self,index):
        return self.heap[self.get_parent_index(index)] 
    def left_child(self,index):
        return self.self.heap[self.get_left_child_index(index)] 
    def right_child(self,index):
        return self.heap[self.get_right_child_index(index)] 
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1] 
    def insert(self,value):
        self.heap.append(value) 
        self.heapify_up(len(self.heap)-1) 
    def heapify_up(self,index):
        while self.has_parent(index)and self.parent(index)>self.heap[index]:
            parent_index = self.get_parent_index(index) 
            self.swap(parent_index,index) 
            index = parent_index 
    def delete_min(self):
        if len(self.heap)==0:
            raise IndexError("Heap is Empty") 
        min_value = self.heap.pop()
        self.heapify_down(0)
        return min_value 
    def heapify_down(self, index):
        # Move the element down until the heap property is restored
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
                smaller_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index 
    def peek(self):
        if len(self.heap)==0:
            raise IndexError("Heap is empty") 
        return self.heap[0] 
    def print_heap(self):
        print("Heap is",self.heap)
h1 = MinHeap() 
h1.insert(10) 
h1.insert(30) 
h1.insert(2) 
h1.insert(90) 
h1.print_heap()
