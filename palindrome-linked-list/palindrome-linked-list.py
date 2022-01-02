# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=''
        h= head
        while h is not None:
            s+= str(h.val)
            h= h.next
        
        s1= s[::-1]
        if s==s1:
            return True
        else:
            return False
        

