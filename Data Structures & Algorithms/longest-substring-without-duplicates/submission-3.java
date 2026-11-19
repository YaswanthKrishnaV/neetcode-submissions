class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l =0, n = s.length();
        Set<Character> hs = new HashSet<>();
        int wl =0;
        for (int i =0; i<n;i++){
            while (hs.contains(s.charAt(i))){
                hs.remove(s.charAt(l));
                l++;
            }
            hs.add(s.charAt(i));
            wl = Math.max(wl, i-l+1);
        }

        return wl;
    }
}
