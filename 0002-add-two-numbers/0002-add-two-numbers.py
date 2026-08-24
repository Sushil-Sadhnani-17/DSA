# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remain = 0

        dummy = ListNode()
        cur = dummy

        while l1 or l2:
            total = remain
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            remain = total // 10
            total = total % 10
            temp = ListNode(total)
            
            cur.next = temp
            cur = temp
        if remain:
            temp = ListNode(remain)
            cur.next = temp
        return dummy.next