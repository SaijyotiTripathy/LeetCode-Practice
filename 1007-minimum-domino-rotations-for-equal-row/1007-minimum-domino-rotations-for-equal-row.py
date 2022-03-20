class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        c= Counter(tops+bottoms)
        c= dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        #print(c)
        num= list(c.keys())[0]
        n= len(tops)
        
        count=0
        print(num)
        
        l1,l2=[],[]
        for i in range(n):
            if num==tops[i] and num==bottoms[i]:
                count+=1
            elif num==tops[i]:
                l1.append(i)
            elif num==bottoms[i]:
                l2.append(i)
        #print(l1,l2)
        
        if n==len(l1+l2)+count:
            return min(len(l1),len(l2))
        else:
            return -1
        
                
        