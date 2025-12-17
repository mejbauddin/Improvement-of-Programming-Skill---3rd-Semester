
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getHeight(node):
    if not node:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))



def isPerfect(node, level, height):

    if not node:
        return True

    if not node.left and not node.right:
        return level == height

    if not node.left or not node.right:
        return False

    return (isPerfect(node.left, level + 1, height) and
            isPerfect(node.right, level + 1, height))



node_0 = TreeNode(1)
node_0.left = TreeNode(2)
node_0.right = TreeNode(3)
node_0.left.left = TreeNode(4)  

h = getHeight(node_0)
print(isPerfect(node_0, 1, h))    



node_0.left.right = TreeNode(123)    
node_0.right.left = TreeNode(321)     
node_0.right.right = TreeNode(999)   

h = getHeight(node_0)
print(isPerfect(node_0, 1, h))        