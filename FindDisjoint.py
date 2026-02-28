class Disjoint:
    def __init__(self,size):
        self.rank=[0]*(size+1)
        self.parent=[0]*(size+1)
        self.size=[1]*(size+1)

        for i in range(size+1):
            self.parent[i]=i
    
    def findUPar(self,u):
        if self.parent[u]==u:
            return u
        r=self.findUPar(self.parent[u])
        self.parent[u]=r
        return r

    def unionRank(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)

        if ulp_u==ulp_v:
            return 

        elif self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
            
    
    def unionSize(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)

        if ulp_u==ulp_v:
            return 

        elif self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=self.size[ulp_v]

d = Disjoint(7)
d.unionSize(1,2)
d.unionSize(2,3)
d.unionSize(4,5)
d.unionSize(6,7)
d.unionSize(5,6)
if d.findUPar(3)==d.findUPar(7):
    print("Same")
else:
    print("Not same")
d.unionSize(3,7)

if d.findUPar(2)==d.findUPar(7):
    print("Same")
else:
    print("Not same")


