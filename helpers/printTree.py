def printTree(cur):

    if cur == None:
        return "failed"

    print(cur.val)
    if cur.left:
        printTree(cur.left)
    if cur.right:
        printTree(cur.right)

    return "success"
