class Disjoint:
    def __init__(self,size):
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
            self.size[ulp_u]+=self.size[ulp_v]


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        d=Disjoint(n)
        for i,j in edges:
            if d.findUPar(i)==d.findUPar(j):
               return [i,j]
            else:
                d.unionSize(i,j)
        return [-1,-1]
        