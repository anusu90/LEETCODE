class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int i=0,j=0,n=nums.size(),sol=0;
        for (i=0;i<32;i++){
            int b=0;
            for(j=0;j<n;j++){
                b += (nums[j]>>i)&1;
            }
            if (b%3==1){
                sol=sol | (1<<i);
            }
        }
        return sol;
    }
};