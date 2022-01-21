class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        i=-1
        knowledge= dict(knowledge)
        res=""
        for k in range(len(s)):
            if s[k]=="(":
                i=k
            elif s[k]==")":
                if s[i+1:k] in knowledge:
                    res+= knowledge[s[i+1:k]]
                    i=-1
                else:
                    res+= "?"
                    i=-1
            elif i==-1:
                res+= s[k]
        
        return res
                