class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        intl= ['0','1','2','3','4','5','6','7','8','9']
        res=[]
        s=''
        for i in word:
            if i in intl:
                s+=i
            else:
                if s!='':
                    res.append(int(s))
                    s=''
        if s!='':
            res.append(int(s))
        #print(res)
        return len(set(res))