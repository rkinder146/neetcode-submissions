class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        int[] arr = nums.clone();
        Arrays.sort(arr);
        while(l<r){
            int c = arr[l]+arr[r]-target;
            if (c==0){
                break;
            }
            if (c<0){
                l++;
            }
            else{
                r--;
            }
        }
        for (int i = 0; i<nums.length; i++){
            if (nums[i] == arr[r]){
                r = i;
                break;
            }
        }
        for (int i = 0; i<nums.length; i++){
            if (nums[i] == arr[l] && i != r){
                l = i;
                break;
            }
        }
        if (l>r){
            int t = r;
            r=l;
            l=t;
        }
        return new int[]{l, r};
    }
}
