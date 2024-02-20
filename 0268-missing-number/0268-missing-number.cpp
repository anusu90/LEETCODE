class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int finalSum = n*(n+1)/2;
        int curr = 0;
        for(int i=0;i<n;i++){
            curr=curr+nums[i];
        }
        return finalSum-curr;
    }
};