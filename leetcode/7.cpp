#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int max_bound = INT_MAX / 10;
        bool negative = 0;
        if (x < 0)
        {
            if (x == INT_MIN)
            {
                return 0;
            }

            negative = 1;
            x = -x;
        }

        int reversed = 0;
        while (x != 0)
        {
            if (reversed > max_bound)
            {
                return 0;
            }

            int reminder = x % 10;
            x /= 10;
            reversed = reversed * 10 + reminder;
        }

        if (negative == 1)
        {
            reversed = -reversed;
        }

        return reversed;
    }
};
