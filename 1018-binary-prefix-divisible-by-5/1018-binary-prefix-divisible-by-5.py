class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l=[]
        s=''
        for i in nums:
            s+=str(i)

            if int(s,2)%5==0:
                l.append(True)
            else:
                l.append(False)
        return l