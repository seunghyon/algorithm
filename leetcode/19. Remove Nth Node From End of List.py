class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self,head:ListNode,n:int):
        if n == 0:
            return head

        length = 0
        node = head
        
        while node:
            length += 1
            node = node.next

        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        
        while length > n :
            node = node.next
            length -= 1
        node.next = node.next.next

        return dummy.next

if __name__ == "__main__":
    print(Solution().removeNthFromEnd())
