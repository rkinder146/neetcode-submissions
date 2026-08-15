class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrs = new HashMap<>();
        for (String s : strs){
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String sorted = new String(c);
            if (!anagrs.containsKey(sorted)){
                anagrs.put(sorted, new ArrayList<>());
            }
            anagrs.get(sorted).add(s);
        }
        return new ArrayList<>(anagrs.values());
    }
}
