class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        while index > 0 and current:
            current = current.next     
            index -=1   
        if current:
            return current.value
        return -1
    
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode    

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        current = self.head
        while current and current.next:
            current = current.next
        if current:  
            current.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, index: int, val: int) -> None:      
        dummy = Node(1)
        dummy.next = self.head
        current= dummy
        while current and index > 0:
            current = current.next
            index -=1
        if not current:
            return
        
        newNode =Node(val)
        newNode.next = current.next
        current.next = newNode
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(-1)
        dummy.next = self.head
        current = dummy
        while index > 0 and current:
            current = current.next
            index -=1
        if not current:
            return 
        if  current.next:
            current.next = current.next.next
        self.head = dummy.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)