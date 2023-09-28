class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(node, resList):
    if node is None:
        return
    inorder(node.left, resList)
    print(node.val)
    resList.append(node.val)
    inorder(node.right, resList)


def preorder(node, resList):
    if node is None:
        return
    print(node.val)
    resList.append(node.val)
    inorder(node.left, resList)
    inorder(node.right, resList)


def postorder(node, resList):
    if node is None:
        return
    inorder(node.left, resList)
    inorder(node.right, resList)
    print(node.val)
    resList.append(node.val)


def leftview(node, resList):
    if node is None:
        return
    print(node.val)
    resList.append(node.val)

    leftview(node.left, resList)
    # leftview(node.right, level + 1, maxLevel, resList)


class BinaryTreeLeftView:
    def __init__(self, node):
        self.head = node
        self.maxLevel = -1

    def leftview(self, actualNode, level, resultList):
        if actualNode is None:
            return
        if self.maxLevel < level:
            self.maxLevel = level
            resultList.append(actualNode.val)

        level += 1
        self.leftview(actualNode.left, level, resultList)
        self.leftview(actualNode.right, level, resultList)


        pass

print("test")


a = BinaryTree("1")
a.left = BinaryTree("2")
a.right = BinaryTree("3")
# a.left.left = BinaryTree("4")
a.left.right = BinaryTree("5")

sa = []
print("inorder")
inorder(a, sa)
print(sa)
sa = []
preorder(a, sa)
print("preorder")
print(sa)
sa = []
postorder(a, sa)
print("postorder")
print(sa)

sa = []
leftview(a, sa)
print("leftview")
print(sa)

test = BinaryTreeLeftView(None)
sa = []
test.leftview(None, 0, sa)
print(sa)