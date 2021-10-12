def printTree(root, width, height):

    if root == None:
        return "failed"

    treeMatrix = [[0] * width]
    for i in range(height - 1):
        treeMatrix.append([0] * width)

    print(treeMatrix)
    treeMatrix[0][width // 2] = root.val

    # print("{0: >{1}}".format(cur.val, width // 2))

    if root.left:
        fillTreeNode(root.left, treeMatrix, width // 2 - (height - 1), height, 1)
    if root.right:
        fillTreeNode(root.right, treeMatrix, width // 2 + (height - 1), height, 1)

    for row in treeMatrix:
        print(row)
    return "success"


def fillTreeNode(cur, treeMatrix, width, height, count):
    # if cur.left and cur.right:
    #     print("{0: >{1}}".format(cur.val, width - 2))

    if count >= len(treeMatrix) or width >= len(treeMatrix[0]) or width < 0:
        return
    treeMatrix[count][width] = cur.val

    count += 1
    if cur.left:
        fillTreeNode(cur.left, treeMatrix, width - (height - count), height, count)
    if cur.right:
        fillTreeNode(cur.right, treeMatrix, width + (height - count), height, count)
