#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> sol;
        if(nums.size()<2){
            sol.push_back(nums[0]);
            return sol;
        }
        int p1=nums[0],p2=nums[1],c1=0,c2=0;
        
        for(int x:nums){
            if(x==p1){
                c1++;
            } else if(x==p2){
                c2++;
            }else if(c1==0){
                p1=x;
                c1++;
            }else if(c2==0){
                p2=x;
                c2++;
            }else {
                c1--;
                c2--;
            }
            
        }
        
        int f1=0,f2=0;
        for (int x:nums){
            if(x==p1){
                f1++;
            }else if(x==p2){
                f2++;
            }
        }
        cout<<p1<<c1<<p2<<c2;

        if(f1>nums.size()/3){
            sol.push_back(p1);
        }
        if(f2>nums.size()/3){
            sol.push_back(p2);
        }
        
        return sol;
        
    }
};