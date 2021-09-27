from tree.treeNode import TreeNode
from helpers.getFactors import getFactors


def findFactors(cur):

    factors = getFactors(cur.val)
    if len(factors) == 1:
        cur.left = TreeNode(factors[0])
        cur.right = TreeNode(factors[0])
        return

    if len(factors) > 0:
        boundary = int((len(factors) + 1) / 2)
        cur.left = TreeNode(factors[boundary - 1])
        cur.right = TreeNode(factors[boundary])

        findFactors(cur.left)
        findFactors(cur.right)

    return
