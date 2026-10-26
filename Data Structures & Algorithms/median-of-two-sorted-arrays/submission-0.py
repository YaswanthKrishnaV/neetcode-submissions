class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+ len(nums2)
        i,j = 0, 0
        nums = []
        while i <len(nums1) and j<len(nums2):

            if nums1[i]< nums2[j]:
                nums.append(nums1[i])
                i+=1
            elif nums1[i]> nums2[j]:
                nums.append(nums2[j])
                j+=1
            else:
                nums.append(nums1[i])
                nums.append(nums2[j])
                i+=1
                j+=1
        print(i,j)
        if i == len(nums1) and j <len(nums2):
            print("end of 1")
            nums += nums2[j:]
        if j == len(nums2) and i <len(nums1):
            print("end of 2")
            nums += nums1[i:]

        print(nums)

        return nums[n//2] if n%2 != 0 else (nums[n//2]+nums[n//2 -1])/2

        