#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
        {
            return false;
        }

        int num = 0;
        int origin = x;
        while (x != 0)
        {
            int reminder = x % 10;
            x /= 10;
            num = num * 10 + reminder;
        }

        if (num == origin)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
