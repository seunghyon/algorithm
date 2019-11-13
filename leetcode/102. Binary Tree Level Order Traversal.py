import queue

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root : TreeNode):
        q = queue.Queue()
        q.put(root)

        result = []

        while q.qsize() != 0 :
            cur = []

            for i in range(q.qsize()):
                node = q.get()
                cur.append(node.val)

                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)

            result.append(cur)

        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))
