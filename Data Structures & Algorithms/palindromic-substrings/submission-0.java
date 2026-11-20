class Solution {
    public int countSubstrings(String s) {
        int resLen = 0, resIdx =0;
        int n = s.length();
        int res = 0;
        for(int i=0;i<n;i++){
            int l =i, r=i;
            while(l>=0 && r<n && s.charAt(l)==s.charAt(r)){
                if(r-l+1> resLen){
                    resIdx = l;
                    resLen = r-l+1;
                }
                l--;
                r++;
                res++;
            }

            l=i; r=i+1;
            while(l>=0 && r<n && s.charAt(l)==s.charAt(r)){
                if(r-l+1 >resLen){
                    resIdx=l;
                    resLen = r-l+1;
                }
                l--;
                r++;
                res++;
            }
        }
        return res;
    }
}
