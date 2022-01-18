class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        l=[]
        for i in points:
            if i[0]==x or i[1]==y:
                l.append(i)
                
        if len(l)==0:
            return -1
        else:
            valid=[]
            mindis=10000
            for i in l:
                dis= abs(x-i[0])+abs(y-i[1])
                if dis<mindis:
                    valid.clear()
                    valid.append(i)
                    mindis=dis
                elif dis==mindis:
                    valid.append(i)
                
            return points.index(valid[0])
        