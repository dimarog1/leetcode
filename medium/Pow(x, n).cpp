class Solution {
public:
    double myPow(double a, int b) {
        if (a == 1) {
        return a;
    }
    if (b == 0) {
        return 1;
    }
    double result = 1;
    if (b < 0) {
        b = abs(b);
        a = 1 / a;
    }
    while (b > 0) {
        if (b % 2 == 0) {
            b /= 2;
            a = a * a;
        }
        else {
            b--;
            result *= a;
        }
    }
    return result;
    }
};