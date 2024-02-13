# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        nxt = head.next
        while nxt :
            while nxt and curr.val == nxt.val:
                nxt = nxt.next
            curr.next= nxt
            curr = curr.next
            if nxt:
                nxt = nxt.next
        return head
            



        