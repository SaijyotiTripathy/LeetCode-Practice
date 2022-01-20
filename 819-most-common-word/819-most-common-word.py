class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph= paragraph.lower()
        paragraph= paragraph.replace("."," ")
        paragraph= paragraph.replace("!"," ")
        paragraph= paragraph.replace("?"," ")
        paragraph= paragraph.replace("'"," ")
        paragraph= paragraph.replace(","," ")
        paragraph= paragraph.replace(";"," ")
        l= paragraph.split()
        print(l)
        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d= list(sorted(d.items(), key=lambda item: item[1], reverse= True))
        print(d)
        for i in d:
            if i[0] not in banned:
                return i[0]
            