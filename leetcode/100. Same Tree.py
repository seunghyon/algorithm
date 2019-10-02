class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q:TreeNode)->bool:
        if not p and not q : return True
        if not p or not q : return False
        if p.val == q.val :
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
        else:
            return False

if __name__=="__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    print(Solution().isSameTree(p,q))
