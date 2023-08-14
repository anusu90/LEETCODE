using namespace std;

class Solution {
public:
    int count (vector<int>& nums,int k){
        int sol=0;
        for (int x:nums){
            if(x>=k){
                sol++;
            }
        }
        return sol;
        
    }
    int findKthLargest(vector<int>& nums, int k) {
        int mx=nums[0],mn=nums[0];
        for(int x:nums){
            if (x>mx){
                mx=x;
            }
            if(x<mn){
                mn=x;
            }
        }
        int s=mn,e=mx,sol=nums[0];
        while(s<=e){
            int mid = (s+e)/2;
            int c = count(nums,mid);
            if(c>=k){
                sol=mid;
                s=mid+1;
            }else{
                e=mid-1;
            }
        }
        return sol;
        
    }
};