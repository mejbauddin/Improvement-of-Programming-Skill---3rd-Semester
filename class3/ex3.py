

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    res = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)      
        res.append(node.val)      
        traverse(node.right)      

    traverse(root)
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(inorder_traversal(root))
