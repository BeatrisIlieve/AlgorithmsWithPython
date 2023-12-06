"""
Problem description:
    Implement the DFS algorithm (Depth-First-Search) to traverse a graph
    and find its connected components (nodes connected either directly, or through other nodes).
    The graph nodes are numbered from 0 to n-1
"""


# Solution:

def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue

    component = []

    dfs(node, graph, visited, component)

    print(f'Connected component: {" ".join([str(x) for x in component])}')

"""
Input:
    9
    3 6
    3 4 5 6
    8
    0 1 5
    1 6
    1 3
    0 1 4
    
    2
"""

"""
Result: 
    Connected component: 6 4 5 1 3 0
    Connected component: 8 2
    Connected component: 7
"""