class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        def search(l,n):
            if n not in l:
                return n
            else:
                i= l.index(n)
                return search(l[i+1:],n*2)
        
        return search(nums,original)

        

        