class Solution {

    public String encode(List<String> strs) {
        StringBuilder code = new StringBuilder();
        code.append(threeCharacterInteger(strs.size()));
        for (int i = 0; i<strs.size(); i++){
            code.append(threeCharacterInteger(strs.get(i).length()));
            code.append(strs.get(i));
        }
        return code.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<String>();
        int size = Integer.parseInt(str.substring(0, 3));
        int last = 3;
        for (int i=0; i<size; i++){
            int length = Integer.parseInt(str.substring(last, last + 3));
            strs.add(i, str.substring(last + 3, last + length + 3));
            last += length + 3;
        }
        return strs;
    }

    private String threeCharacterInteger(int x){
        return ""  + (x/100)%10 + (x/10)%10 + x%10;
    }   
}
