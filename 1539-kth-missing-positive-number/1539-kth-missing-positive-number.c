int findKthPositive(int* arr, int arrSize, int k){
    int i=1,pos=0;
        int n = arrSize;
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