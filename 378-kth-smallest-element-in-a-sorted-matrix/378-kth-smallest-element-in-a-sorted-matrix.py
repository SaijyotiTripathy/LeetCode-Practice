class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        for i in matrix:
            l+=i
        print(l)
        l.sort()
        
        return l[k-1]