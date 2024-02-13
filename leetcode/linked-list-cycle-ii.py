# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        thereIs = False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                thereIs = True
                break
        if thereIs:
            start = head
            while start != fast:
                start = start.next
                fast = fast.next
            return start
        return None
        