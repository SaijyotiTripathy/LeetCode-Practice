class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        two=0
        for i in nums:
            two= two^i
        
        two= two & -two
        
        p1,p2=0,0
        for i in range(len(nums)):
            if (nums[i] & two)>0:
                p1= p1^nums[i]
            else:
                p2= p2^nums[i]
        
        return [p1,p2]
        