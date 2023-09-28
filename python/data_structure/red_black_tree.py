# Neighbor
#     Parent or child.
# Ancestor
#     A node reachable by repeated proceeding from child to parent.
# Descendant
#     A node reachable by repeated proceeding from parent to child. Also known as subchild.
# Degree
#     For a given node, its number of children. A leaf has necessarily degree zero.
# Degree of tree
#     The degree of a tree is the maximum degree of a node in the tree.
# Distance
#     The number of edges along the shortest path between two nodes.
# Level
#     The level of a node is the number of edges along the unique path between it and the root node.[2]
# Width
#     The number of nodes in a level.
# Breadth
#     The number of leaves.
# Forest
#     A set of n ≥ 0 disjoint trees.
# Ordered tree
#     A rooted tree in which an ordering is specified for the children of each vertex.
# Size of a tree
#     Number of nodes in the tree.

# There arent any cycle in the graph
# There arent any backwards edge

# inorder: left, value, right
# preorder: value, left, right
# postorder: left, right, value

# Binary tree
# in which each node has at most two children,

# Binary search tree
# ordered or sorted binary tree


class Node:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    def search(self, value):
        node = self
        if node == None or node.val == value:
            return node
        if value < node.val:
            self.search(node.left, value)
        else:
            self.search(node.right, value)

# Red-Black tree
# a kind of self-balancing binary search tree
class RedBlackTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = val
        self.isRed = True
        self.parent = None

#Heap (min/maX) HALOM
# like binary tree just top-bottom order not left right

#HashTable ->dict, map szinte minden egyes mogotte linked list van

#Stack verem LIFO

#Queue FIFO

#Graph G=(v, e)
# V = {NODES}
# E = {EDGES}