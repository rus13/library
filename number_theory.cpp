

int gcd (int a, int b) {
    return b ? gcd (b, a % b) : a;
}

int lcm (int a, int b) {
    return a / gcd(a, b) * b;
}

int gcd(int a, int b, int & x, int & y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }
    int x1, y1;
    int d = gcd(b % a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return d;
}
