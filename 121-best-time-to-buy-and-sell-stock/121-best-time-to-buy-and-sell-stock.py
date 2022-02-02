class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        res = 0
        while r < len(prices):
            curr = prices[r] - prices[l] 
            if prices[l] < prices[r]:
                res =max(curr, res)
            else:
                l = r
            r+= 1
        return res