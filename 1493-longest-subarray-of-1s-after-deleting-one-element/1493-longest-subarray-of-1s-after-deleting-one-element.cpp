using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int start=0, end=0;
        int count_of_zero=0;
        int sol=0;
        while (end<nums.size()){
            if(nums[end]==0){
                count_of_zero++;
            }
            if(count_of_zero==2){
                sol = max (sol,end-start-1);
                while(count_of_zero==2){
                    if(nums[start]==0){
                        count_of_zero--;
                    }
                    start++;
                }
            }
            end++;
        }
        return max(sol,end-start-1);
    }
};