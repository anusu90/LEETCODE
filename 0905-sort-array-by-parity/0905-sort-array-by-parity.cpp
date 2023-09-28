class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int start=0,end=nums.size()-1;
        while (start<end){
            if(nums[end]%2==0){
                if(nums[start]%2!=0){
                    int temp=nums[start];
                    nums[start]=nums[end];
                    nums[end]=temp;
                    start++;
                    end--;
                }else{
                    start++;
                }
            }else{
                end--;
            }
            
        }
        return nums;
    }
    
};