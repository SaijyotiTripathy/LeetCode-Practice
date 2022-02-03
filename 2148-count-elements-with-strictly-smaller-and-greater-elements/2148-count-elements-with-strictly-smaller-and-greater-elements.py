class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=0
        c+= nums.count(max(nums))
        c+= nums.count(min(nums))
        n= len(nums)
        
        if n-c<0:
            return 0
        return n-c
        