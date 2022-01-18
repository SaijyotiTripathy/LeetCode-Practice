class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        flowerbed= [0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                c+=1
                flowerbed[i]=1
            #print(flowerbed)
        
        if c>=n:
            return True
        else:
            return False
        