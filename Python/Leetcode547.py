class Leetcode547:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = 1
            for j in range(n):
                if isConnected[i][j]==1 and visited[j]==0:
                    dfs(j)


        n = len(isConnected)
        result = 0
        # number of nodes
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                result += 1
            
        return result