# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        h=head
        l=[]
        while h is not None:
            l.append(h.val)
            h=h.next
        
        l[k-1],l[len(l)-k]= l[len(l)-k],l[k-1]
        
        head= ListNode()
        node= head
        for i in l:
            node.next= ListNode(i)
            node= node.next
        return head.next
        