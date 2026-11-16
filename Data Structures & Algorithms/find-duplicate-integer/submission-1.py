class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for num in nums:
        #     idx = abs(num)-1
        #     if nums[idx]<0:
        #         return num

        #     nums[idx]*=-1
        #     print(nums)
        # return -1
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print(slow, fast)
            if slow == fast:
                break

        slow2= 0
        while True:
            slow  = nums[slow]
            slow2 = nums[slow2]
            # print(slow, slow2)
            if slow == slow2:
                return slow 