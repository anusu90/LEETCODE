#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> ust1{};
        unordered_set<int> ust2{};
        for (auto x :nums1){
            ust1.insert(x);
        }
        for (auto x:nums2){
            ust2.insert(x);
        }
        vector<int>v1{};
        vector<int>v2{};
        for (auto x:nums1){
            if(ust2.count(x)==0 && ust1.count(x)==1){
                v1.push_back(x);
                ust1.erase(x);
            }
        }
        for(auto x:nums2){
            if(ust1.count(x)==0 && ust2.count(x)==1){
                v2.push_back(x);
                ust2.erase(x);
            }
        }
        vector<vector<int>>sol{v1,v2};
        return sol;
    }
};