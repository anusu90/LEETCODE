class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int n = nums.size();
        int i;
        if(n<=2){
            return true;
        }
        bool isDec=true,isInc=true;
        for(i=1;i<n;i++){
            if(nums[i]<nums[i-1]){
                isInc=false;
            }
        }
        for(i=1;i<n;i++){
            if(nums[i]>nums[i-1]){
                isDec=false;
            }
        }
        return isInc || isDec;
    }
};