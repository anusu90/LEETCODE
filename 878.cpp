using namespace std;
class Solution {
public:
    int nthMagicalNumber(int A, int B, int C) {
    long lcm = B * C / __gcd(B, C), l = 2, r = 1e14, mod = 1e9 + 7,ans;
    while(l<=r){
        long mid = (l+r)/2;
        if( mid/B + mid/C - mid/lcm < A){
            l=mid+1;
        } else {
            ans = mid;
            r=mid-1;
        }
    }
    return ans%1000000007;
        
    }
};