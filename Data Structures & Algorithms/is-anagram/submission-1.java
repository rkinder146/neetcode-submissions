class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sarr = s.toCharArray();
        char[] tarr = t.toCharArray();

        Arrays.sort(tarr);
        Arrays.sort(sarr);
        return Arrays.equals(sarr, tarr);
    }
}
