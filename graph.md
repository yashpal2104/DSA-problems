# Graph cheatsheet

## 🔵 BFS CHEAT SHEET
When to Use BFS

- Shortest path

- Level-by-level traversal

- Nearest thing / minimum steps

- Grid spreading problems (fire, rot, distance)

## BFS TEMPLATE (MEMORIZE)
```py
from collections import deque

queue = deque()
queue.append(start)
visited = set([start])

while queue:
    node = queue.popleft()
    for neighbor in neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### BFS KEYWORDS (INTERVIEW)

- Queue

- FIFO

- Level order

- Distance / steps

## 🔴 DFS CHEAT SHEET
When to Use DFS:

- Explore entire structure

- Count components

- Path existence

- Backtracking problems

### DFS TEMPLATE (MEMORIZE)
```py
def dfs(node):
    if node is invalid:
        return
    mark node visited
    for neighbor in neighbors(node):
        dfs(neighbor)
```
### DFS KEYWORDS (INTERVIEW)

- Recursion

- Stack

- Go deep

- Backtracking