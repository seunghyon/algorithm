import queue

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root : TreeNode):
        if not root:
            return 0
        if not root.left or not root.right :
            return 1
        
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1

        return max(depth_left, depth_right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))
