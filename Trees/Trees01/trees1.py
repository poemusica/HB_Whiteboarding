class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def set_value(self, number):
        self.value = number

def depth_first_traversal(node):
    if node is None:
        return
    print node.value,

    depth_first_traversal(node.left)
    depth_first_traversal(node.right)


def breadth_first_traversal(node):
    q = []
    q.append(node)
    while q:
        n = q.pop(0)
        print n.value

        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    

def depth_first_search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True

    return depth_first_search(node.left, target) or depth_first_search(node.right, target)

def breadth_first_search(node, target):
    q = []
    q.append(node)

    while q:
        n = q.pop(0)
        if n.value == target:
            return True
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

# TEST
root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.left = BinaryTreeNode(2)
root.left.left.left = BinaryTreeNode(3)
root.left.left.right = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(7)
root.right.left.left = BinaryTreeNode(8)
root.right.left.right = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(10)

# breadth_first_traversal(root)
# depth_first_traversal(root)

# print depth_first_search(root, 12)
# print breadth_first_search(root, 12)