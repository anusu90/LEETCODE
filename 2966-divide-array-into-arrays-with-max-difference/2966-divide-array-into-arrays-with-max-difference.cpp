#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> sol;
        int n=nums.size(),currSize=0;
        vector<int> temp;
        int currIndex = 0;
        
        for(int i=0;i<n;i++){
            if(currSize==3){
                sol.push_back(temp);
                temp={};
                temp.push_back(nums[i]);
                currSize=1;
                currIndex=1;
            }else{
                if(currIndex==0){
                    temp.push_back(nums[i]);
                    currSize++;
                    currIndex++;
                }else{
                    if (nums[i]- temp[0] > k){
                        sol={};
                        return sol;
                    }else{
                        temp.push_back(nums[i]);
                        currSize++;
                        currIndex++;
                    }
                }
                
            }
        }
        sol.push_back(temp);
        return sol;
    }
};