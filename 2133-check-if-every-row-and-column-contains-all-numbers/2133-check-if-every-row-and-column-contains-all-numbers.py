class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n= len(matrix)
        l=[]
        for i in range(n):
            l1=[]
            for j in range(n):
                l1.append(matrix[j][i])
            l1.sort()
            l.append(l1)
        
        r=[]
        for i in matrix:
            i.sort()
            r.append(i)
        print(r,l)
        
        check=[[i for i in range(1,n+1)] for j in range(n)]
        if r==check and l==check:
            return True
        else:
            return False