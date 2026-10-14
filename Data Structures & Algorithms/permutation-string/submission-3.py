class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_h = [0]*26
        s2_h = [0]*26
        for i in range(len(s1)):
            print(i)
            s1_h[ord(s1[i])- ord('a')]+=1
            s2_h[ord(s2[i])- ord('a')]+=1
        if s1_h == s2_h:
            return True
        for i in range(len(s1),len(s2)):
            s2_h[ord(s2[i-len(s1)])- ord('a')]-=1
            s2_h[ord(s2[i])- ord('a')]+=1
            print(s1_h,s2_h)
            if s1_h == s2_h:
                return True
        return False



        