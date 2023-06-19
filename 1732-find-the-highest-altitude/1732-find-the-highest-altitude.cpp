class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int m {0},curr{0};
        for (int x:gain){
            curr = curr+x;
            if(curr>m){
                m=curr;
            }
        }
        return m;
        
    }
};