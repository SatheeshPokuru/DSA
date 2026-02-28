class Solution:
    
    """def dfs(self,node,adj_list,vis,st):
        vis[node]=1
        
        for n in adj_list[node]:
            if vis[n]==0:
                self.dfs(n,adj_list,vis,st)
                
        st.append(node)"""
        
    def topoSort(self, V, edges):
        # Code here
        from collections import deque
        q=deque()
        adj_list=[]
        
        for i in range(V):
            adj_list.append([])
            
        for i,j in edges:
            adj_list[i].append(j)
        
        """vis=[0]*V
        
        st=[]
        
        for i in range(V):
            if vis[i]==0:
                self.dfs(i,adj_list,vis,st)
        
        return st[::-1]"""
        
        indegree=[0]*V
        topo=[]
         
        for i in range(V):
            for node in adj_list[i]:
                indegree[node]+=1
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
            
       
        while q:
           node=q.popleft()
           topo.append(node)
           
           for i in adj_list[node]:
               indegree[i]-=1
               if indegree[i]==0:
                   q.append(i)
                   
        return topo
        
                
        
        