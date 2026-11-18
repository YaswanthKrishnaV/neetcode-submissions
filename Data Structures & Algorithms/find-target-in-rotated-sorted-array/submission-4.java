class Solution {
    public int bs( int l, int r, int[] nums){
        while (l<r){
            int mid = (l+r)/2;
            if (nums[mid] > nums[r]){
                l = mid+1;
            }else{
                r= mid;
            }

        }
        return l;
    }
    public int search(int[] nums, int target) {
        int l =0, r = nums.length -1;

        int pivot = bs(l,r, nums);
        if (nums[pivot]<=target && target<=nums[r]){
            l= pivot;
        }else{
            r = pivot-1;
        }
        
        while (l<=r){
            int mid = (l+r)/2;
            if (nums[mid]==target){
                return mid;
            }else if (nums[mid]<target){
                l = mid+1;
            }else{
                r= mid-1;
            }

        }
        return -1;
    }
}
