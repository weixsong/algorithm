#include <iostream>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int idx = 0;
        while (str[idx] == ' ')
        {
            idx++;
        }

        bool negative = false;

        if (str[idx] == '-')
        {
            negative = true;
            idx++;
        }
        else if (str[idx] == '+')
        {
            idx++;
        }

        int num = 0;
        while (idx < str.size())
        {
            int d = str[idx] - 48;
            if (d < 0 || d > 9)
            {
                break;
            }

            int new_num = num * 10 + d;
            if (new_num / 10 != num)
            {
                // overflow
                if (negative == true)
                {
                    return INT_MIN;
                }
                else
                {
                    return INT_MAX;
                }
            }

            num = new_num;
            idx++;
        }

        if (negative == true)
        {
            num = -num;
        }

        return num;
    }
};
