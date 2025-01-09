import heapq 
#THE PRIORITY QUEUE USING MINHEAP IN THIS MODULE BY DEFAULT 
priority_Queue = [] 
heapq.heappush(priority_Queue,(2,"Eat breakfast"))
heapq.heappush(priority_Queue,(1,"wakeup"))
heapq.heappush(priority_Queue,(3,"Go to work")) 
print(priority_Queue) 
while priority_Queue:
    priority,task = heapq.heappop(priority_Queue)
    print(f"Task:{task}, priority:{priority}") 