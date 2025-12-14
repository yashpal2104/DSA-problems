def numIslands(self, grid: List[List[str]]) -> int:
        # bfs

        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()

            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]


                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
    
# dfs
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count