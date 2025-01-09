import heapq 
#Creating a priorityQueue empty  
priorityQueue = []  
#adding elements to the priorityQueue 
heapq.heappush(priorityQueue,(-2,"Eat breakfast")) 
heapq.heappush(priorityQueue,(-1,"Wake up")) 
heapq.heappush(priorityQueue,(-3,"Go to work")) 
#removing the elements from the queue as per the priority 
while priorityQueue:
    task,priority = heapq.heappop(priorityQueue) 
    print(f"Task: {task},priority:{priority}") 

