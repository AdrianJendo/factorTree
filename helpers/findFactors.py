from tree.treeNode import TreeNode
from helpers.getFactors import getFactors


def findFactors(cur, height=1):

    factors = getFactors(cur.val)
    if len(factors) == 1:
        cur.left = TreeNode(factors[0])
        cur.right = TreeNode(factors[0])
        return height + 1

    if len(factors) > 0:
        boundary = int((len(factors) + 1) / 2)
        cur.left = TreeNode(factors[boundary - 1])
        cur.right = TreeNode(factors[boundary])
        height += 1
        height = max(findFactors(cur.left, height), findFactors(cur.right, height))

    return height
