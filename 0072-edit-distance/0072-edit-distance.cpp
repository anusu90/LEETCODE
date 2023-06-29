#include <vector>
using namespace std;
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1,0));
        for(int i=0;i<=n;i++){
            dp[0][i]=i;
        }
        for (int j=0;j<=m;j++){
            dp[j][0]=j;
        }
        
        for(int j=1;j<=m;j++){
            for(int i=1;i<=n;i++){
                if(word1[i-1]==word2[j-1]){
                    dp[j][i]=dp[j-1][i-1];
                }else{
                    dp[j][i]=min({dp[j-1][i-1],dp[j][i-1],dp[j-1][i]})+1;
                }
            }
        }
        return dp[m][n];
    }
};