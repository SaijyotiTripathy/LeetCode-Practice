class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='{' or i=='[' or l==[]:
                l.append(i)
            elif i==')' and l[-1]=='(':
                l.pop()
            elif i=='}' and l[-1]=='{':
                l.pop()
            elif i==']' and l[-1]=='[':
                l.pop()
            else:
                l.append(i)
        
        if l==[]:
            return True
        else:
            return False