class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length()) return false;
        // HashMap<Character, Integer> c1 = new HashMap<>();
        // HashMap<Character, Integer> c2 = new HashMap<>();
        int[] c1 = new int[26];
        int[] c2 = new int[26];
        for(int i=0;i<s1.length();i++){
            // c2.put(s2.charAt(i),c2.getOrDefault(s2.charAt(i),0)+1);
            // c1.put(s1.charAt(i),c1.getOrDefault(s1.charAt(i),0)+1);
            c1[s1.charAt(i)-'a']++;
            c2[s2.charAt(i)-'a']++;
        }
        if (Arrays.equals(c1,c2)) return true;

        int l=0;

        for(int r = s1.length();r<s2.length();r++){
            c2[s2.charAt(r-s1.length()) - 'a']--;
            c2[s2.charAt(r)-'a']++;
            if (Arrays.equals(c1,c2)) return true;
        }

        return false;
    }
}
