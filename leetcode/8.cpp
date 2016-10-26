#include <iostream>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int begin = 0;
        while (str[begin] == ' ')
        {
            begin++;
        }

        long max_int = INT_MAX;
        long min_int = INT_MIN;

        bool negative = false;

        if (str[begin] == '-')
        {
            negative = true;
            begin++;
        }
        else if (str[begin] == '+')
        {
            begin++;
        }

        long number = 0;
        while (begin < str.size())
        {
            char c = str[begin];
            int d = c - 48;
            if (d < 0 || d > 9)
            {
                break;
            }

            number = number * 10 + d;
            begin++;

            if (negative == true)
            {
                if (-number <= min_int)
                {
                    return min_int;
                }
            }
            else
            {
                if (number >= max_int)
                {
                    return max_int;
                }
            }
        }

        if (negative == true)
        {
            number = -number;
        }

        if (number >= max_int)
        {
            return max_int;
        }

        if (number <= min_int)
        {
            return min_int;
        }

        return number;
    }
};

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
