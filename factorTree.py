import sys
from tree.treeNode import TreeNode
from helpers.findFactors import findFactors
from helpers.printTree import printTree
from helpers.findWidth import findWidth


def factorTree():
    # num = int(sys.argv[1])
    num = 72
    root = TreeNode(num)
    cur = root

    if root.val < 0:
        root.left = TreeNode(-1)
        root.right = TreeNode(-1 * root.val)
        cur = root.right

    height = findFactors(cur)
    width = findWidth(root)

    printTree(root, width, height)  # Responsible for printing the tree to console
    return root


factorTree()
