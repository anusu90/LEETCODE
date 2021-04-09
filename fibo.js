function fibo(n) {
    let a = 1, b = 1
    if (n <= 2) return 1;
    for (i = 3; i <= n; i++) {
        [a, b] = [b, a + b]
    }
    return b
}