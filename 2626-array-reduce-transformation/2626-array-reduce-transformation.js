/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let sol=init;
    for(i=0;i<nums.length;i++){
        sol = fn(Number(sol),Number(nums[i]));
    }
    return sol;
    
};