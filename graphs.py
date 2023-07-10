from collections import deque 

# 1.Depthfirsttraversal(iteratively)

# def dfprint(graph,start):
#     stack = [start]
#     while stack:
#         current = stack[-1]
#         print(current)
#         stack.pop()
#         for neighbor in graph[current]:
#             stack.append(neighbor)


#2. Depthfirsttraversal(recursively)

# def dft(graph,current):
#     print(current)
#     for neighbor in graph[current]:
#         dft(graph,neighbor)

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

bft(graph,'a')

# a -> c
# |    |
# v    v
# b <- e
# |    |
# v    V
# d <- f 