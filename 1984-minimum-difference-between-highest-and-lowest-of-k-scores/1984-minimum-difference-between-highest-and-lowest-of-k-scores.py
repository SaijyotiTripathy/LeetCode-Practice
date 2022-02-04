class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k==1:
            return 0
        nums.sort()
        
        m=nums[-1]-nums[0]
        for i in range(len(nums)-k+1):
            #print(i,nums[i:i+k])
            if nums[i:i+k][-1]-nums[i:i+k][0] < m:
                m= nums[i:i+k][-1]-nums[i:i+k][0]
        return m