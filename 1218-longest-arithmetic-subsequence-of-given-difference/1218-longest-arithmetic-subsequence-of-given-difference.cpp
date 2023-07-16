#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int,int> dp={};
        int sol=1;
        for(int x:arr){
            int search = x - difference;
            if(dp.count(search)!=0){
                dp[x] = dp[search]+1;
            }else{
                dp[x]=1;
            }
            sol = max(sol,dp.at(x));

        }
        return sol;
    }
};