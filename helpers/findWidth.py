spacing = 2


def findWidth(root, width=0):
    if root != None:
        width += len(str(root.val)) + spacing

    cur = root

    while cur.left:
        cur = cur.left
        width += len(str(cur.val)) + spacing

    cur = root
    while cur.right:
        cur = cur.right
        width += len(str(cur.val)) + spacing

    return width
