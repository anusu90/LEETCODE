/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let sol = []
    function recurr(arr,d){
        for(let i=0;i<arr.length;i++){
            if(Array.isArray(arr[i]) && d<n){
                recurr(arr[i],d+1)
            }else{
                sol.push(arr[i])
            }
        }
    }
    recurr(arr,0);
    return sol;
    
};