#class Creation 
#Class is a Blue print to create objects 
class Flower():
    def __init__(self,name,petals,price):
        self.name=name
        self.petals=petals
        self.price=price
    def setname(self,name):
        self.name=name
    def setpetals(self,petals):
        self.petals=petals
    def setprice(self,price):
        self.price=price
    def getname(self):
        return self.name
    def getpetals(self):
        return self.petals
    def getprice(self):
        return self.price   
f=Flower("lilly",24,14) #object Creation 
print(f.getname())
print(f.getpetals())
print(f.getprice())



#overloading

def add(d,*args):
    if d=='int':
        s=0
    elif d=="str":
        s=" "
    for i in args:
        s=s+i
    print(s)
add('int',5,6)
add("str",'5','6')