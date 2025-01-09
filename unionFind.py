class unionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)] 
        self.rank = [1]*n 
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 
    def union(self,x,y):
        rootx = self.find(x) 
        rooty = self.find(y) 
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.parent[rooty] = self.parent[rootx] 
            elif self.rank[rootx]<self.rank[rooty]:
                self.parent[rootx] = self.parent[rooty] 
            else:
                self.parent[rooty] = rootx 
                self.rank[rootx]+=1
    def connected(self,x,y):
        return self.find(x)==self.find(y) 
    

uf1 = unionFind(5) 
uf1.union(0,1) 
uf1.union(1,2)  
print(uf1.connected(0,3)) 