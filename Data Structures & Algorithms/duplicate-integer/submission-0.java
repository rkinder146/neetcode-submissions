class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> occ = new HashMap<>();
        for (int x : nums){
            occ.merge(x, 1, Integer::sum);
            if (occ.get(x) > 1){
                return true;
            }
        }
        return false;
    }
}