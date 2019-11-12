class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def validBST(self,root, minValue, maxValue):
        if not root:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self.validBST(root.left,minValue,root.val) and self.validBST(root.right,root.val,maxValue)

    def isValidBST(self,root:TreeNode):
        return self.validBST(root,float('-inf'),float('inf'))


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(Solution().isValidBST(root))
