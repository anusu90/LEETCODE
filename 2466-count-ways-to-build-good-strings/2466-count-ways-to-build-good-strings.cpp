#include <vector>
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int mod = 1000000007;
        vector<int> dp (high+1,0);
        dp.at(0)=1;
        for(int i=0;i<high+1;i++){
            int cz = i-zero;
            if(cz>=0){
                dp[i] = ((dp[i]%mod)+ (dp[cz]%mod)%mod);
            }
            int co=i-one;
            if(co>=0){
                dp[i] =  ((dp[i]%mod)+ (dp[co]%mod)%mod);
            }
        }
        int sol=0;
        for(int i=low;i<high+1;i++){
            sol = (sol%mod + dp[i]%mod)%mod;
        }
        return sol;
    }
};