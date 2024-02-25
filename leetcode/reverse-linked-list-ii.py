# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy,head
        i = 1
        while curr:
            if left == i:
                break
            prev ,curr = curr, curr.next
            i += 1
        i =1
        curr = dummy.next
        arr =[]
        while curr and i <= right:     
            if i >= left and i <= right:
                arr.append(curr)
            curr = curr.next     
            i +=1   
        if arr:
            arr[0].next = arr[-1].next
            for i in range(len(arr)-1, 0, -1):
                arr[i].next = arr[i-1]
            prev.next = arr[-1]
        return dummy.next


            
        