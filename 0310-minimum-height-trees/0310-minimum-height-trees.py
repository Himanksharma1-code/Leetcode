class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves