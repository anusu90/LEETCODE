class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int s=0,e=numbers.size()-1;
        while(s<e){
            if (numbers[s]+numbers[e]==target){
                return {s+1,e+1};
            }
            if (numbers[s]+numbers[e]>target){
                e--;
            }else{
                s++;
            }
        }
        return {-1,-1};
        
    }
};
