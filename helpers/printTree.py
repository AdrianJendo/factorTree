def printTree(cur, width):

    if cur == None:
        return "failed"

    print("{0: >{1}}".format(cur.val, int(width / 2)))

    # print(cur.val)
    # if cur.left:
    #     printTree(cur.left)
    # if cur.right:
    #     printTree(cur.right)

    return "success"
