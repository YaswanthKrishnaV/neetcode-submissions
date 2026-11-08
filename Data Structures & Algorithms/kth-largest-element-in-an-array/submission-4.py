class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
    

        # return nums[k-1]
        # return heapq.nlargest(k,nums)[-1]

        heap = nums[:k]

        heapq.heapify(heap)
        # print(heap)
        for num in nums[k:]:
            if num> heap[0]:
                heapq.heapreplace(heap, num)

            # print(heap)
        return heap[0]
        