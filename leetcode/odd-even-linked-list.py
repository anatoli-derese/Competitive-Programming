# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ctr = 1
        odd = dummy
        dummy2 = ListNode()
        even = dummy2
        curr = head
        while curr:
            if ctr % 2 :
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            ctr +=1
            curr = curr.next
        even.next = None
        odd.next = dummy2.next
        return dummy.next