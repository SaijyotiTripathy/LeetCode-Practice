class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        while maxDoubles>0 and target>1:
            if target%2==0:
                maxDoubles-=1
                target= target//2
                c+=1
            else:
                target-=1
                c+=1
        
        if target>1:
            c+= target-1
        
        return c
        