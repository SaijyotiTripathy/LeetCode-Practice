class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        i=0
        while len(stones)>1:
            
            if stones[i]==stones[i+1]:
                stones.remove(stones[i])
                stones.remove(stones[i])

            else:
                if stones[i]>stones[i+1]:
                    stones[i]-=stones[i+1]
                    stones.remove(stones[i+1])
                    
                elif stones[i]<stones[i+1]:
                    stones[i+1]-=stones[i]
                    stones.remove(stones[i])
                stones.sort(reverse=True)
        
        if len(stones)==0:
            return 0
        else:
            return stones[0]
        