#include <iostream>
#include <sstream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1)
        {
            return s;
        }

        int cycle = 2 * (numRows - 1);
        stringstream ss;
        for (int i = 0; i < numRows; i++)
        {
            if (i >= s.size())
            {
                break;
            }

            int idx = i;
            int step1 = cycle - (i << 1);
            int step2 = cycle - step1;
            while (idx < s.size())
            {
                ss << s[idx];
                if (step1 == 0 || step2 == 0)
                {
                    idx += cycle;
                    continue;
                }

                idx += step1;
                if (idx < s.size())
                {
                    ss << s[idx];
                    idx += step2;
                }
            }
        }

        return ss.str();
    }
};
