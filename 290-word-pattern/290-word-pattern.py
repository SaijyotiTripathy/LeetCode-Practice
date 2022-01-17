class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1,d2={},{}
        for i in range(len(pattern)):
            if pattern[i] in d1:
                d1[pattern[i]].append(i)
            else:
                d1[pattern[i]]=[i]
        
        l=s.split(" ")
        for i in range(len(l)):
            if l[i] in d2:
                d2[l[i]].append(i)
            else:
                d2[l[i]]=[i]
        
        #print(list(d1.values()),list(d2.values()))
        if list(d1.values())== list(d2.values()):
            return True
        else:
            return False