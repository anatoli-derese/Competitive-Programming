# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(1)
        dummy.next = head
        current = dummy 
        while n >= 0 and current: 
            n -=1
            current = current.next
        back = dummy
        while current :
            current = current.next
            back = back.next
        if back.next:
            back.next = back.next.next
        return dummy.next