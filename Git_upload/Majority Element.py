class Solution {
    public int majorityElement(int[] nums) {
        int cont=0;
        for(int i=0;i<nums.length;i++){
            cont=0;
            for(int j=0;j<nums.length;j++){
                if(nums[i]==nums[j])
                cont+=1;
            }
            if(cont>(nums.length/2))
            return nums[i];
        }
     return -1;
    }

}