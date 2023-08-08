#include <iostream>
using namespace std;
class Solution {
public:
    int binarySearch(int s, int e,int target, vector<int>&nums){
        cout<<"s"<<s<<"e"<<e<<endl;
        if (s>e) return -1;
        int mid = (s+e)/2;
        if(nums[mid]==target) {
            return mid; 
        } else if (nums[mid]>target){
            return binarySearch(s,mid-1,target,nums);
        } else {
            return binarySearch(mid+1,e,target,nums);
        }
    }
    int search(vector<int>& nums, int target) {
        int s=0,e=nums.size()-1,sol = 0;
        while(s<=e){
            int mid = (s+e)/2;
            if(nums[mid]>=nums[0]){
                sol=mid;
                s=mid+1;
            }else{
                e=mid-1;
            }
        }
        int ans = binarySearch(0,sol,target,nums);
        if(ans!=-1) return ans;
        return binarySearch(sol+1,nums.size()-1,target,nums);
    }
};