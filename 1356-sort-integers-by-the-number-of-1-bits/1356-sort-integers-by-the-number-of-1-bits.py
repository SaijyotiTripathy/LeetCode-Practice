class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d={}
        for i in arr:
            c= bin(i).count("1")
            if c in d:
                d[c].append(i)
            else:
                d[c]=[i]
        d= dict(sorted(d.items()))
        l=[]
        for i in d:
            d[i].sort()
            l+= d[i]
        
        return l
            
        
        