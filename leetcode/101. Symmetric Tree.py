class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isMirror(self,t1,t2):
        if not t1 and not t2 : return True
        if not t1 or not t2 : return False
        if t1.val == t2.val :
            return self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left)
        else:
            return False
        
    def isSymmetric(self,root:TreeNode)->bool:
        return self.isMirror(root,root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    print(Solution().isSymmetric(root))
