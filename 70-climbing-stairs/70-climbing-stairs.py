class Solution:
    def climbStairs(self, n: int) -> int:
        memory={}
        def memoize(c):
            def inner(num):
                if num not in memory:
                    memory[num]=c(num)
                return memory[num]
            return inner
            
        @memoize
        def count(n):
            if n<0:
                return 0
            elif n==0:
                return 1
            else:
                return count(n-2)+count(n-1)
            
        return count(n)