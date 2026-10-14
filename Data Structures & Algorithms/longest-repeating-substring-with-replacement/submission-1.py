class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r =0,0
        maxf = 0
        maxl = 0
        hashmap = [0]*26

        while r<len(s):
            hashmap[ord(s[r])-ord("A")]+=1
            maxf = max(maxf,hashmap[ord(s[r])-ord("A")])
            if r-l+1 - maxf > k:
                hashmap[ord(s[l])-ord("A")]-=1 
                l+=1
            if r-l+1 - maxf <= k:
                maxl = max(r-l+1,maxl)
            r+=1

        return maxl


        