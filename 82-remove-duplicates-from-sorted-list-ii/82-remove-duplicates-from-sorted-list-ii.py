# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l,l1= [],[]
        h=head
        
        while h is not None:
            if h.val not in l:
                l.append(h.val)
            else:
                l1.append(h.val)
            h= h.next
        #print(l)
        
        r= list(set(l).difference(set(l1)))
        r.sort()
        head= ListNode()
        node= head
        for i in r:
            node.next= ListNode(i)
            node= node.next
        
        return head.next