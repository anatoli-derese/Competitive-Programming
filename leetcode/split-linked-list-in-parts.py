# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next
        n = (length//k) + 1
        first = length % k
        arr =[]
        temp = head
        while first > 0:
            first -= 1
            arr.append(temp)
            while n > 1 and temp:
                temp = temp.next
                n -= 1
            if temp:
                temp.next, temp = None, temp.next
            n = (length//k) + 1
        rest = (k - (length % k))
        while rest > 0:
            rest -=1
            arr.append(temp)
            n = (length // k)
            while n > 1 and temp:
                temp = temp.next
                n -=1
            if temp:
                temp.next , temp = None, temp.next
        return arr