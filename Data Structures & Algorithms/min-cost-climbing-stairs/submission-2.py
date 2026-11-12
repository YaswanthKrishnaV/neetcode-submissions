class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        # # dp = [0]*(n+1)

        # prev, curr = 0, 0

        # for i in range(1,n+1):
        #     print(prev, curr)
        #     curr, prev = min(prev+cost[i-1], curr+cost[i-2]), curr
        #     print(prev, curr)

        for i in range(n-3,-1,-1):
            cost[i]= cost[i] +min(cost[i+1], cost[i+2])
            print(cost)

        return min(cost[0], cost[1])