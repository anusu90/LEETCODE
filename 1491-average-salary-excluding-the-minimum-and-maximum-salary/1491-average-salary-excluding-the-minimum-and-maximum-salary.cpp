#include <limits>
#include <iostream>
using namespace std;
class Solution {
public:
    double average(vector<int>& salary) {
        double mx = INT_MIN;
        double mi = INT_MAX;
        int n = salary.size();
        double s=0;
        for (double x:salary){
            if (x>mx){
                mx=x;
            }
            if(x<mi){
                mi=x;
            }
            s+=x;
        }
        
        return (s-mx-mi)/(n-2);
        
    }
};