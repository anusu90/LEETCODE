using namespace std;
#include <vector>;

class Solution {
public:
    int recur(int st,int e, vector<vector<int>>& dp,string& s){
            if(st==e){
                dp[st][e]=1;
            }
            if(st>e){
                return 0;
            }
            if(dp[st][e]==-1){
                if(s[st]==s[e]){
                    dp[st][e]=2+recur(st+1,e-1,dp,s);
                }else{
                    dp[st][e]= max(recur(st,e-1,dp,s),recur(st+1,e,dp,s));
                }
            }
            return dp[st][e];
        }
    int longestPalindromeSubseq(string s) {
        int l=s.size();
        vector<int> temp(l,-1);
        vector<vector<int>> dp(l,temp);
        return recur(0,l-1,dp,s);
        
    }
};