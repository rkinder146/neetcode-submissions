class Solution {
    class FrequencyPair implements Comparable<FrequencyPair>{
        private int freq;
        private int value;
        public FrequencyPair(int f, int v){
            freq = f;
            value = v;
        }
        public int compareTo(FrequencyPair other){
            return Integer.compare(freq, other.freq);
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(int i : nums){
            freq.merge(i, 1, Integer::sum);
        }
        PriorityQueue<FrequencyPair> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i : freq.keySet()){
            pq.add(new FrequencyPair(freq.get(i), i));
        }
        int[] ans = new int[k];
        for (int i=0; i<k; i++){
            ans[i]=pq.poll().value;
        }
        return ans;
    }
}
