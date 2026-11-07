class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # ans = []
        # sub = []
        # def dfs(i):
        #     if i>=n:
        #         ans.append(sub.copy())
        #         return 

        #     sub.append(nums[i])
        #     print(ans,i)
        #     dfs(i+1)
        #     sub.pop()
        #     dfs(i+1)

        # dfs(0)
        # return ans

        res = [[]]

        for num in nums:
            res+=[sub + [num] for sub in res]
            print(res)

        return res

        