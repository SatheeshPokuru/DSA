class Solution(object):
    def dfs(self,node,adj_list,vis,st,path_vis):
        vis[node]=1
        path_vis[node]=1

        for n in adj_list[node]:
            if vis[n]==0:
                rv=self.dfs(n,adj_list,vis,st,path_vis)
                if rv==False:
                    return False
            
            if path_vis[n]==1:
                return False
                           
        st.append(node)
        path_vis[node]=0
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list=[] #n      
        n=len(prerequisites) 
        vis=[0]*numCourses  #n
        st=[]   #n
        path_vis=[0]*numCourses     #n

        for i in range(numCourses):
            adj_list.append([])         

        for i,j in prerequisites:
            adj_list[j].append(i)

        for i in range(numCourses):     #O(V+E)
            if vis[i]==0:
                rv=self.dfs(i,adj_list,vis,st,path_vis)
                if rv==False:
                    return []

        return st[::-1]

        