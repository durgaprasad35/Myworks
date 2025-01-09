queue = [] 
def new_customer(Customer_id):
    queue.append(Customer_id) 
    print(f"The customer with customerid {Customer_id} enter into the queue")  
def serve_customer():
    if len(queue)!=0:
        a=queue.pop(0) 
        print(f"The custmer with custmer_id {a} is left the queue") 
new_customer(1)
new_customer(2) 
new_customer(3) 
new_customer(90) 
new_customer(5) 
serve_customer() 
serve_customer() 
serve_customer() 
serve_customer() 
serve_customer() 

