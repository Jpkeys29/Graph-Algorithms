from collections import deque 

# 1.Depthfirsttraversal(iteratively)

def dft(graph,start):
    stack = [start]
    while stack:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)


# 2. Depthfirsttraversal(recursively)

def dft(graph,current):
    print(current)
    for neighbor in graph[current]:
        dft(graph,neighbor)

# 3. Breadthfirsttraversal
def bft(graph,start):
    queue = deque([start])
    while queue:
        current =queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# a -> c
# |    |
# v    v
# b <- e
# |    |
# v    V
# d <- f 


        # ---------------------------------------


# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.


# def adj_list(edges):
#     graph = {}
#     for edge in edges:
#         a,b = edge
#         if a not in graph:
#             graph[a] = []
#         if b not in graph:
#             graph[b] = []
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph
# print(adj_list(edges))

# Converting a list of tuples into an Adjacency list

# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

        # ----------------------------------------
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

def connected_components_count(graph):
  count = 0
  visited = set()
  for current in graph: # Iteration to hop to the separate components
    if helper(graph,current,visited) == True:
      count +=1
  return count
    
def helper(graph,current,visited): #helper function to fully traverse a component
  if current in visited:
    return False
  visited.add(current)
  
  for neighbor in graph[current]:
    helper(graph,neighbor,visited)
  return True

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
