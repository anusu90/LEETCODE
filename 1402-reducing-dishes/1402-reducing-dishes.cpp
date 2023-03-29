#include <vector>;
using namespace std;
class Solution {
public:
    int maxSatisfaction(vector<int>& v) {
        sort(v.begin(),v.end());
        int s=v.size();
        vector<int> prefixSum(s,0);
        for (int i=s-1;i>=0;i--){
            prefixSum[i]=i+1<s?v[i]+prefixSum[i+1]:v[i];
        }
        int maxVal{0};
        int currVal{0};
        for (int i=0;i<s;i++){
            cout<<prefixSum[i]<<endl;
            maxVal=maxVal + ((i+1)*v[i]);
        }
        currVal=maxVal;
        for (int i=0;i<s;i++){
            currVal -= prefixSum[i];
            maxVal=max(maxVal,currVal);
        }
        return maxVal;
        
    }
};