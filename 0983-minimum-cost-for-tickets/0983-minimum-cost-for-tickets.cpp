#include<vector>
using namespace std;
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int last_day{days.back()},i,k=0;
        vector<int>dp(last_day,0);
        for(i=0;i<last_day;i++){
            int j =i+1;
            if(j<days[k]){
                if(i==0){
                    continue;
                }else{
                    dp[i]=dp[i-1];
                }
            }else{
                int f = i-1>=0?dp[i-1]+costs[0]:costs[0];
                int s = i-7>=0?dp[i-7]+costs[1]:costs[1];
                int t=i-30>=0?dp[i-30]+costs[2]:costs[2];
                dp[i]=min({f,s,t});
                k++;
            }
            cout<<dp[i]<<endl;
        }
        return dp.back();

    }
};