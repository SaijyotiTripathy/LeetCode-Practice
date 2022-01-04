class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        c= int(log(n,2))
        mask=0
        for i in range(c):
            mask= (mask<<1)|1
        
        return (~n)&mask
        