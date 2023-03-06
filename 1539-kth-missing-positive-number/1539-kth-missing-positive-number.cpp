class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int i=1,pos=0;
        int n = arr.size();
        while(pos<n && k>0){
            if(arr[pos]==i){
                i++;
                pos++;
            }else{
                k--;
                i++;
            }
        }
        i--;
        return i+k;
        
    }
};