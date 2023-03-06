/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    let i=1
    let pos=0;
    let n = arr.length;
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
    
};