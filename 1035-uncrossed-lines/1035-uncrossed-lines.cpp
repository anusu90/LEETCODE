#include <vector>

class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        vector<int> v (n+1,0);
        vector<vector<int>> dp(m+1,v);
        
        for(int j=1;j<m+1;j++){
            for(int i=1;i<n+1;i++){
             if(nums1[i-1]==nums2[j-1]){
                 dp[j][i]=dp[j-1][i-1]+1;
             }else{
                 dp[j][i]=max(dp[j][i-1],dp[j-1][i]);
             }
            }
        }
        return dp[m][n];
    }
};