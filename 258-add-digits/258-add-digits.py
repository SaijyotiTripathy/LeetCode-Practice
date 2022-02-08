class Solution:
    def addDigits(self, num: int) -> int:
        s = list(str(num))
        if len(s) == 1:
            return num
        while len(s) > 1:
            total = 0
            for i in s:
                total += int(i)
            s = list(str(total))
        return int(s[0])
        
        