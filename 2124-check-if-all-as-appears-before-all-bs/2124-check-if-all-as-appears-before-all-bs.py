class Solution:
    def checkString(self, s: str) -> bool:
        a,b=0,0
        for i in s:
            if i=='a' and b>0:
                return False
            if i=='a':
                a+=1
            if i=='b':
                a=0
                b+=1
        return True
        