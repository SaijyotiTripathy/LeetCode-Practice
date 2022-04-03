class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max= max(nums)
        new_max= 0
         
        for i in range(0, len(nums)):
            new_max = new_max + nums[i]
            if new_max < 0:
                new_max = 0
                
            elif (curr_max < new_max):
                curr_max = new_max
                 
        return curr_max
        