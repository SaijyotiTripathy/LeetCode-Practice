class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
            if nums[i]>target:
                return l
        return l