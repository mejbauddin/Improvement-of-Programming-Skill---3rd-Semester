class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getHeight(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

root = TreeNode(15)
root.left = TreeNode(7)
root.right = TreeNode(20)
root.left.left = TreeNode(9)
root.left.right = TreeNode(3)


print("Maximum depth:", getHeight(root))  