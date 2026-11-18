class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Map<Integer,Integer> hm = new HashMap<>();

        // for(int i=0;i< numbers;i++){
        //     int rem = target - numbers[i];
        //     if (hm.containsKey(temp)){
        //         return new int[] {map.get(temp), i+1};
        //     }else{
        //         mp.put(numbers[i], i+1);
        //     }
        // }

        int l =0, r = numbers.length -1;
        while(l<r){
            int curSum = numbers[l] + numbers[r];
            if (curSum> target){
                r--;
            }else if (curSum < target){
                l++;
            } else{
                return new int[] {l+1, r+1};
            }
        }
        return new int[0];
        
    }
}
