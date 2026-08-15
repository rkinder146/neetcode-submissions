class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrs = new HashMap<>();
        for (String s : strs){
            int[] freq = new int[26];
            for (char i : s.toCharArray()){
                freq[i-'a']++;
            }
            String sorted = Arrays.toString(freq);
            if (!anagrs.containsKey(sorted)){
                anagrs.put(sorted, new ArrayList<>());
            }
            anagrs.get(sorted).add(s);
        }
        return new ArrayList<>(anagrs.values());
    }
}
