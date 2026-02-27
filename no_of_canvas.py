class Solution(object):
    def levelByLevel(self,grid,bfs,vis,m,n,dirs):
        while bfs:
            for _ in range(len(bfs)):
                node=bfs.popleft()
                r=node[0]
                c=node[1]

                for i,j in dirs:
                    nr=r+i
                    nc=c+j
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1 and vis[nr][nc]==0:
                        bfs.append((nr,nc))
                        vis[nr][nc]=1
            
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m=len(grid)
        n=len(grid[0])
        bfs=deque()
        vis=[]
        cnt=0

        for _ in range(m):
            vis.append([0]*n)
        
        for i in range(m):
            if grid[i][0]==1 and vis[i][0]==0:
                bfs.append((i,0))
                vis[i][0]=1
        
        for i in range(m):
            if grid[i][n-1]==1 and vis[i][n-1]==0:
                bfs.append((i,n-1))
                vis[i][n-1]=1
        
        for j in range(n):
            if grid[0][j]==1 and vis[0][j]==0:
                bfs.append((0,j))
                vis[0][j]=1
        
        for j in range(n):
            if grid[m-1][j]==1 and vis[m-1][j]==0:
                bfs.append((m-1,j))
                vis[m-1][j]=1
        
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        
        self.levelByLevel(grid,bfs,vis,m,n,dirs)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==0:
                    cnt+=1
        
        return cnt
        