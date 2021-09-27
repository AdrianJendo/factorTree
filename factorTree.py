import sys
from tree.treeNode import TreeNode
from helpers.findFactors import findFactors


def printFactorTree():
    # num = int(sys.argv[1])
    num = -72
    root = TreeNode(num)
    cur = root

    if root.val < 0:
        root.left = TreeNode(-1)
        root.right = TreeNode(-1 * root.val)
        cur = root.right

    findFactors(cur)

    # print(factors)
    # return factors

    # while num > 1:

    print(root)  # Responsible for printing the tree to console
    return root


printFactorTree()
