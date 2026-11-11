class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 1

        for i in range(1,n):
            print(prev, curr)
            curr, prev = prev + curr, curr        
            print(prev, curr)
        return curr
        