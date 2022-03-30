class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r= len(matrix)-1
        c=0
        while r>-1 and c<len(matrix[0]):
            if target<matrix[r][c]:
                r-=1
            elif target>matrix[r][c]:
                c+=1
            else:
                return True
        return False