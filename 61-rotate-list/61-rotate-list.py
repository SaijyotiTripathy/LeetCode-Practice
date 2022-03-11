# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        l=[]
        h=head
        while h is not None:
            l.append(h.val)
            h= h.next
        
        n=len(l)
        if len(l)>k:
            l1= l[n-k:]+l[:n-k]
        elif len(l)<k:
            k=k%len(l)
            l1= l[n-k:]+l[:n-k]
        else:
            l1=l
        #print(l1)
            
        head= ListNode()
        node= head
        for i in l1:
            node.next= ListNode(i)
            node= node.next
        
        return head.next