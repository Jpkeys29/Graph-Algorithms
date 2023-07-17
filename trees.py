from collections import deque #deque is a double-ended queue

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def dft(root):
# The first iteration finishes when reaching "b" children. Because 'd' does not have any children.
    if root is None: return[]
    output =[]
    stack = [root]
    while stack:
        current = stack.pop()
        output.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return output

#Recusive dft:
def dft(root):
    if root is None:
        return []
    left_vals= dft(root.left)
    right_vals= dft(root.right)
    return [root,*left_vals,*right_vals]
    # Alternative return:
    # return [root.val]+left_vals+right_vals

# Breadth First Traversal
def bft(root):
    if not root: return []
    output = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        output.append(current.val)
        if current.left:
            output.append(current.left)
        if current.right:
            output.append(current.right)
    return output




 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(dft(a))
#        a
#      /  \
#     b   c
#   / \    \
#  d  e    f  