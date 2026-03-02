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
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edges = []

        n = len(points)
        for i in range(n):      #O((n*n-1)/2)
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((cost, i, j))
        
        edges.sort()
        d=Disjoint(n)
        wt=0

        for w,i,j in edges:
            if d.findUPar(i)!=d.findUPar(j):
                d.unionSize(i,j)
                wt+=w
        
        return wt
