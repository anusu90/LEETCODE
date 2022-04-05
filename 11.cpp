class Solution {
public:
    int maxArea(vector<int>& A) {
        int l=0,r=A.size()-1,area= 0,curr;
        while(l<r){
            if(A[l]>A[r]){
                curr=(r-l)*A[r];
            }else{
                curr=(r-l)*A[l];
            }
            if(curr>area){
                area=curr;
            }
            
            if(A[l]<A[r]){
                l++;
            } else{
                r--;
            }
        }
        return area;
        
    }
};