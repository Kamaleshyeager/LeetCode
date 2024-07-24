class Solution {
    public int xorSubsets(int index, int[] nums, int val){
        if(index == nums.length) return val;
        int include = xorSubsets(index+1,nums,val^nums[index]);
        int exclude = xorSubsets(index+1,nums,val);
        return include+exclude;
    }
    public int subsetXORSum(int[] nums) {
        return xorSubsets(0,nums,0);
    }
}