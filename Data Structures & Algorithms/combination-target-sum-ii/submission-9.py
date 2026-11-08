class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def dfs(i,curr, total):
            # print(i,curr, total)
            
            if total == target:
                res.add(tuple(curr))
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j]== candidates[j-1]:
                    continue
                if candidates[j] + total> target:
                    return
                
                curr.append(candidates[j])
                dfs(j+1, curr, total+candidates[j])
                curr.pop()
            # while i+1 < len(candidates) and candidates[i]== candidates[i+1]:
            #     i +=1
            # dfs(i+1, curr, total)

        dfs(0,[],0)

        return [list(combination) for combination in res]
        