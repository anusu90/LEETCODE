// Running Sum of 1d Array

var runningSum = function (nums) {

    let sum = 0, runningSum = [];
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i]
        runningSum.push(sum)
    }
    return runningSum
};