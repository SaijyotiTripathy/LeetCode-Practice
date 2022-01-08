class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in costs:
            if coins>0:
                coins-=i
                c+=1
        
        if coins>=0:
            return c
        else:
            return c-1
        