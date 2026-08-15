class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> occ = new HashMap<>();
        for (int x : nums){
            if (occ.containsKey(x)){
                return true;
            }
            else{
                occ.put(x, 1);
            }
        }
        return false;
    }
}