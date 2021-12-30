class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s1=''
        j=0
        for i in range(len(s)):
            #print(s1)
            if j<len(spaces):
                if (i==spaces[j]):
                    s1+=' '
                    j+=1
                s1+=s[i]
            else:
                s1+=s[i]
        
        return s1