

function SecondLargest(x) {
    let max = x[0]
    let max2 = x[1]
    for (let i = 2; i < x.length; i++) {
        if (max < max2) [max, max2] = [max2, max]
        if (x[i] > max) [max2, max] = [max, x[i]]
        if (x[i] > max2 && x[i] < max) max2 = x[i]
    }
    return max2
}
