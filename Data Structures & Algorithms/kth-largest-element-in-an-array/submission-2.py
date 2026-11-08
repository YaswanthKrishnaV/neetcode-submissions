class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
    

        # return nums[k-1]
        return heapq.nlargest(k,nums)[-1]

        