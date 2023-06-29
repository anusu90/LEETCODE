#include <vector>
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();
        vector<int> temp (n+1,0);
        vector<vector<int>> dp (m+1, temp);
        for(int i=1;i<m+1;i++){
            for(int j=1;j<n+1;j++){
                if(text1[j-1]==text2[i-1]){
                    dp[i][j]=dp[i-1][j-1]+1;
                }else{
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }
};