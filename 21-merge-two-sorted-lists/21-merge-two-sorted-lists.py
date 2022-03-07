# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        h1,h2= list1,list2
        
        while h1 is not None:
            l.append(h1.val)
            h1= h1.next
        while h2 is not None:
            l.append(h2.val)
            h2= h2.next
        l.sort()
        
        head= ListNode()
        node= head
        
        for i in l:
            node.next= ListNode(i)
            node= node.next
        return head.next
        