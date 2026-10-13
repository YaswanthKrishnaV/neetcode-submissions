class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        if n==0:
            return 0
        # leftmax = [0]*n
        # rightmax = [0]*n

        # leftmax[0]= height[0]
        # for i in range(1,n):
        #     leftmax[i]= max(leftmax[i-1],height[i])

        # rightmax[-1] =height[-1]
        # for i in range(n-2,-1,-1):
        #     rightmax[i] = max(rightmax[i+1],height[i])

        # res = 0
        # for i in range(n):
        #     res+=min(leftmax[i],rightmax[i])-height[i]

        # return res 
        # stack = []
        # res = 0

        # for i in range(n):
        #     while stack and height[i]>=height[stack[-1]]:
        #         mid = height[stack.pop()]
        #         if stack:
        #             r = height[i]
        #             l = height[stack[-1]]
        #             h = min(l,r)- mid
        #             w = i - stack[-1] - 1
        #             res+=h*w
        #     stack.append(i)

        # return res

        res = 0
        l,r= 0, n-1
        lm, rm = height[l], height[r]
        while l<r:
            if lm<rm:
                l+=1
                lm = max(lm, height[l])
                res+=lm - height[l]

            else:
                r-=1
                rm=max(rm,height[r])
                res+=rm-height[r]

        return res


        