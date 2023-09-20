class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int mx = -1;
        int tmp = 0;
        bool k = true;

        for (int i = 0; i < seats.size(); ++i) {
            if (seats[i] == 0) {
                tmp++;
            }
            else {
                if (k) {
                    k = false;
                    mx = tmp;
                    tmp = 0;
                    continue;
                }
                tmp = ((tmp / 2 - 1) + tmp % 2) + 1;
                mx = mx < tmp ? tmp : mx;
                tmp = 0;
            }
        }

        return mx < tmp ? tmp : mx;
    }
};