class Solution(object):
    def dfs(self,node,adj_list,vis,path_vis):
        vis[node]=1
        path_vis[node]=1

        for n in adj_list[node]:
            if vis[n]==0:
                rv=self.dfs(n,adj_list,vis,path_vis)
                if rv==False:
                    return False
                       
            elif path_vis[n]==1:
                return False

        path_vis[node]=0
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list=[]       
        n=len(prerequisites)
        vis=[0]*numCourses
        path_vis=[0]*numCourses

        for i in range(numCourses):
            adj_list.append([])

        for i,j in prerequisites:
            adj_list[i].append(j)
        
        for i in range(numCourses):
            if vis[i]==0:
                rv=self.dfs(i,adj_list,vis,path_vis)
                if rv==False:
                    return False
        
        return True

        
        

        
