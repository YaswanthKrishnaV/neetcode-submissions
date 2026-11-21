class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);
        int res =0;
        int lastend = intervals[0][1];

        for (int i =1; i<intervals.length;i++){
            lastend = Math.min(lastend,intervals[i-1][1]);
            if(lastend>intervals[i][0]){
                res++;
            }else{
                lastend = intervals[i][1];
            }
        }
        return res;
    }
}
