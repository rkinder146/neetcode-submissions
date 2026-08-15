class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrs = new HashMap<>();
        for (String s : strs){
            char[] freq = new char[26];
            for (int i=0; i < s.length(); i++){
                freq[s.charAt(i)-'a']++;
            }
            String sorted = new String(freq);
            if (!anagrs.containsKey(sorted)){
                anagrs.put(sorted, new ArrayList<>());
            }
            anagrs.get(sorted).add(s);
        }
        return new ArrayList<>(anagrs.values());
    }
}
