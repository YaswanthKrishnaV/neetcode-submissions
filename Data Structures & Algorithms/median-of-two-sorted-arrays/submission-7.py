class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+ len(nums2)
        i,j = 0, 0
        nums = []
        m1 = m2 = 0
        for c in range((n//2)+1):
            m2 = m1
            if i<len(nums1) and j < len(nums2):
                print("ij",i,j)
                if nums1[i]> nums2[j]:
                    m1 = nums2[j]
                    j+=1
                else:
                    m1 = nums1[i]
                    i+=1
            elif i < len(nums1):
                print("i",i)
                m1= nums1[i]
                i+=1
            else:
                print("j",j)
                m1= nums2[j]
                j+=1

        # if i == len(nums1) and j <len(nums2):
        #     print("end of 1")
        #     nums += nums2[j:]
        # if j == len(nums2) and i <len(nums1):
        #     print("end of 2")
        #     nums += nums1[i:]

        # print(nums)

        # return nums[n//2] if n%2 != 0 else (nums[n//2]+nums[n//2 -1])/2
            print(m1,m2)
        if n%2==1:
            return float(m1)
        else:
            return (m1+m2)/2.0

        