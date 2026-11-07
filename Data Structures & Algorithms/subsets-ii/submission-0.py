class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        sub = []

        def dfs(i):
            if i>=n:
                res.append(sub.copy())
                return

            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            idx= i+1
            while (idx<n and nums[idx]==nums[idx-1]):
                idx+=1

            dfs(idx)

        dfs(0)

        return res        