class Solution:
    def safeNodes(self, V, edges):
        # Code here
        from collections import deque
        adj_list=[]
        for i in range(V):
            adj_list.append([])
        vis=[0]*V
        indegree=[0]*V
        
        for i,j in edges:
            adj_list[j].append(i)
        
        for i in range(V):
            for node in adj_list[i]:
                indegree[node]+=1
        
        q=deque()
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        
        while q:
            node=q.popleft()
            ans.append(node)
            
            for n in adj_list[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        return ans
                
        
        