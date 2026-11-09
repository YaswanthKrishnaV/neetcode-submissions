class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        visit = set()

        # def dfs(r,c):
        #     if (r< 0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visit):
        #         return 0

        #     visit.add((r,c))
        #     return (1+ dfs(r+1,c) + dfs(r,c-1) + dfs(r-1,c) + dfs(r, c+1))

        def bfs(r,c):
            q = deque()
            grid[r][c]=0
            q.append((r,c))
            res=1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if (nr< 0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0):
                        continue

                    q.append((nr,nc))
                    grid[nr][nc]=0
                    res+=1

            return res
        

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = max(area, bfs(r,c))

        return area

        