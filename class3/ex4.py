
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


prev = None

def isBST(root):
    global prev
    prev = None   
    return inorder_check(root)


def inorder_check(node):
    global prev

    if not node:
        return True

    if not inorder_check(node.left):
        return False

    if prev is not None and node.val <= prev:
        return False

    prev = node.val

    return inorder_check(node.right)



node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)    

print(isBST(node))   

bst_node = TreeNode(8)
bst_node.left = TreeNode(3)
bst_node.right = TreeNode(10)
bst_node.right.left = TreeNode(9)
bst_node.right.right = TreeNode(14)

print(isBST(bst_node))  

