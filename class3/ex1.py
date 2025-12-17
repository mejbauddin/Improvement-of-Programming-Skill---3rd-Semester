class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, node_15, node_7)
node_9 = TreeNode(9)
node_0 = TreeNode(3, node_9, node_20)

print(node_0.val)  
print(node_0.left.val, node_0.right.val)  
print(node_0.right.left.val, node_0.right.right.val) 