# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyOne = Node(0)
        dummyTwo = Node(0)
        front = dummyOne
        back = dummyTwo
        curr = head
        while curr:
            if curr.val < x:
                front.next = curr
                front = front.next
            else:
                back.next = curr
                back =  back.next
            curr = curr.next
        back.next = None
        front.next= dummyTwo.next
        return dummyOne.next

        


        
        