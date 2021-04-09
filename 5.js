/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    let dp = [...new Array(s.length)].map(v => new Array(s.length).fill(false));
    let lps = ""
    for (i = 0; i < s.length; i++) {
        dp[i][i] = true
    }
    lps = s[0]
    for (i = 0; i < s.length - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true
            lps = s.substring(i, i + 2)
        }
    }
    let k = 3;
    while (k <= s.length) {
        for (i = 0; i < s.length - k + 1; i++) {
            j = i + k - 1;
            if (dp[i + 1][j - 1] === true && s[i] === s[j]) {
                dp[i][j] = true;
                lps = s.substring(i, j + 1)
            }
        }
        k++
    }
    return lps
};