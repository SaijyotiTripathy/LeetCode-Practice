class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n= Counter(nums)
        
        n= dict(sorted(n.items(), key=lambda item: item[1], reverse=True))
        
        return list(n.keys())[:k]