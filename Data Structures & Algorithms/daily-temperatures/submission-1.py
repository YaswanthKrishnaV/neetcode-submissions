from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = deque()
        res = [0]*len(temperatures)
        c = 0
        for i, temp in enumerate(temperatures):
            while queue and temp>queue[-1][0]:
                t,j = queue.pop()
                res[j] = i-j
                
            queue.append((temp,i))
        return res

