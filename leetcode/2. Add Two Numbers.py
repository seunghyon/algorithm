class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        sum = 0
        result = temp = ListNode(0)

        while l1 or l2 or sum != 0:
            if l1:
                sum = l1.val
                l1 = l1.next
            if l2:
                sum = l2.val
                l2 = l2.next

            temp.next = ListNode(sum % 10)
            sum = sum // 10
            temp = temp.next

        return result.next
        
