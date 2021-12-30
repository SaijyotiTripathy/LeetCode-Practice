# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        h=head
        while h is not None:
            h= h.next
            c+=1
        
        for i in range(c//2):
            head= head.next
        return head