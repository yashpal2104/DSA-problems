# dfs approach
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            duplicate = Node(curr.val)
            visited[curr] = duplicate
            
            for neighbor in curr.neighbors:
                    duplicate.neighbors.append(dfs(neighbor))
            return duplicate

        return dfs(node)