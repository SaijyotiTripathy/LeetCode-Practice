class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        size= len(str(n))
        c= Counter(str(n))
        
        for i in range(30):
            if len(str(2**i))==size:
                c1= Counter(str(2**i))
                if c==c1:
                    return True
            if len(str(2**i))>size:
                return False
        return False