class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self,n:int):
        if n == 0:
            return []
        return self.BST(1,n)

    def BST(self,left,right):
        if left > right :
            return [None]

        result = []

        for i in range(left,right+1):
            left_nodes = self.BST(left,i-1)
            right_nodes = self.BST(i+1,right)
            print(left_nodes,' ',right_nodes)

            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    result.append(root)

        return result


if __name__ == "__main__":
    n = 3
    print(Solution().generateTrees(n))
