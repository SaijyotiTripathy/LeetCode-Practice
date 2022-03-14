class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n= len(matrix),len(matrix[0])
        row,col= m-1,0
        
        while col<n and row>=0:
            if matrix[row][col]>target:
                row-=1
            elif matrix[row][col]<target:
                col+=1
            elif matrix[row][col]==target:
                return True
        return False
                
        