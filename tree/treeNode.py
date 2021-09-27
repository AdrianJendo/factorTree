from helpers.printTree import printTree


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return printTree(self)
