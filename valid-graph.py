def validTree(self, n, edges):
    if not n:
        return True
    adj = {i:[] for i in range(n)}
    count = 0
    
    visited = set()
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
        
    def dfs(node, prev):
        if node in visited:
            return False
        
        visited.add(node)
        
        for j in adj[node]:
            if j == prev:
                continue
            if not dfs(j, node):
                return False
        return True
    
    return dfs(0, -1) and n == len(visited)