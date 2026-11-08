class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # stones.sort()
        # queue = deque() 
        # if len(stones)==1:
        #     return stones[0]

        # for i in range(len(stones)-2,-1,-1):
        #     print(i,stones)
        #     if stones[i+1]==stones[i]:
        #         stones[i]= 0
                
        #     else:
        #         stones[i]= abs(stones[i] - stones[i+1])
        #     print(i,stones)
        
        # return stones[0]
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second> first:
                heapq.heappush(stones,first - second)
                # print(stones)
            
        stones.append(0)
        return abs(stones[0])

        