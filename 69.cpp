class Solution {
public:
    int mySqrt(int x) {
        long l=1,r=1e9,sol=0;
        while(l<=r){
            long mid = (l+r)/2;
            if(mid*mid==x){
                return mid;
            } else if (mid*mid<x){
                sol = mid;
                l=mid+1;
            } else{
                r=mid-1;
            }
        }
        return sol;
        
    }
};