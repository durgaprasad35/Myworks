from queue import PriorityQueue 
pq = PriorityQueue() 
#adding elements to the priorityqueue 
pq.put((1,"Amma")) 
pq.put((2,"Wife")) 
pq.put((3,"Family")) 
while not pq.empty():
    priority,task = pq.get() 
    print(f"Processsing: {task} with priority{priority}") 

