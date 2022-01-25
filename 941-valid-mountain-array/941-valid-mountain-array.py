class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        if arr.count(max(arr))>1:
            return False
        ind= arr.index(max(arr))
        
        l1,l2=[],[]
        a1,a2= arr[:ind], arr[ind+1:]
        #print(a1,a2)
        if a1==[] or a2==[]:
            return False
        
        a11= list(set(a1))
        a11.sort()
        a22= list(set(a2))
        a22.sort(reverse=True)
        #print(a11,a22)
        if a11==a1 and a22==a2:
            return True
        else:
            return False