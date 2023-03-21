class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        int curr_len{0};
        double long final_count{0};
        for (int x:nums){
            if(x==0){
                curr_len++;
                final_count+=curr_len;
            }else{
                curr_len=0;
            }
        }
        return final_count;
    }
};