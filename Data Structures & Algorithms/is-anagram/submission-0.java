class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> counts = new HashMap<>();
        if (s.length() != t.length()){return false;}
        for (int i = 0; i < s.length(); i++){
            counts.merge(s.charAt(i), 1, Integer::sum);
        }
        for (int i = 0; i < t.length(); i++){
            counts.merge(t.charAt(i), -1, Integer::sum);
            if (counts.get(t.charAt(i))<0){
                return false;
            }
        }
        return true;
    }
}
