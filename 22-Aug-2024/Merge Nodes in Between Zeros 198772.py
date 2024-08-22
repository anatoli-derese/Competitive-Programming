# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        fast = head.next
        prev = None
        while curr and fast:
            temp = 0
            while  fast.val != 0:
                temp += fast.val
                fast = fast.next
            curr.val = temp
            fast = fast.next
            prev = curr
            curr = curr.next
        prev.next = None
        return head
