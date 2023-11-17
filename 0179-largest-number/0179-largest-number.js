/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let s = nums.sort((a,b)=>{
        const n1 = Number(a+""+b)
        const n2 = Number(b+""+a)
        if(n1>n2){
            return -1
        }
        return 1
    })
    
    sol=""
    s.forEach((a)=>{
        if(sol==="0" && a===0){
            return
        }
        sol+=a;
    })
    
    return sol
};