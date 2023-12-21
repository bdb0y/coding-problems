
# url: https://codeforces.com/problemset/problem/1904/E

# TODO optimize the DFS traversal and we're good!

n, q = [int(x) for x in input().split()]

graph = {}

for _ in range(n-1):
    node_a, node_b = input().split()
    
    g_keys = graph.keys()
    
    if node_a in g_keys:
        graph[node_a].add(node_b)
        if node_b in g_keys:
            graph[node_b].add(node_a)
        else:
            graph[node_b] = set()
            graph[node_b].add(node_a)
    else:
        graph[node_a] = set()
        graph[node_a].add(node_b)
        
        if node_b in g_keys:
            graph[node_b].add(node_a)
        else:
            graph[node_b] = set()
            graph[node_b].add(node_a)

def DFS(graph, root_node, removed=set(), visited=None, counts=None, count=0):
    if visited == None:
        visited = set()
        counts = set()
    
    visited.add(root_node)
    counts.add(count)
    
    count += 1
    
    for adj_node in graph[root_node] - removed - visited:
        DFS(graph, adj_node, removed, visited, counts, count)
        
    return visited, counts
        

for _ in range(q):
    query = input().split()
    
    starting_node = query[0]
    
    nodes_to_remove = int(query[1])
    
    removed = []
    if nodes_to_remove > 0:
        removed = query[2:]
    
    traversal, counts = DFS(graph, starting_node, set(removed))
    print(max(counts))
