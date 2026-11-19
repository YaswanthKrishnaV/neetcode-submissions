class Solution {
    public int trap(int[] height) {
        int n = height.length;
        if (n==0){
            return 0;
        }
        int l=0, r= n-1;
        int lm = height[0];
        int rm = height[n-1];

        // for (int i =1; i<n; i++){
        //     lm[i] =  Math.max(lm[i-1],height[i]);
        // }
        // rm[n-1] = height[n-1];
        // for (int i =n-2; i>=0; i--){
        //     rm[i] =  Math.max(rm[i+1],height[i]);
        // }

        // int res=0;
        // for(int i=0;  i<n; i++){
        //     res+=Math.min(lm[i],rm[i]) - height[i];
        // }
        // return res;
        int res=0;
        while(l<r){
            if (lm<rm){
                l++;
                lm = Math.max(lm, height[l]);
                res+= lm - height[l];
            }else{
                r--;
                rm = Math.max(rm,height[r]);
                res+= rm- height[r];
            }
        }
        return res;


        
    }
}
