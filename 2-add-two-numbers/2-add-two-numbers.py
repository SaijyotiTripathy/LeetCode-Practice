# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2= "",""
        while l1 is not None:
            n1+= str(l1.val)
            l1= l1.next
        while l2 is not None:
            n2+= str(l2.val)
            l2= l2.next
        #n1,n2= n1[::-1], n2[::-1]
        s= str(int(n1[::-1])+int(n2[::-1]))[::-1]
        #s= s[::-1]
        #print(s)
        
        curr = ListNode(int(s[0]))
        head = curr
        for i in s[1:]:
            temp = ListNode(int(i))
            curr.next = temp
            curr = temp
        
        return head
        
        