#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string longest = "";
        for (int i = 0; i < s.size(); i++)
        {
            string r1 = find(s, i, i);
            if (r1.size() > longest.size())
            {
                longest = r1;
            }

            if (i < s.size() - 1 && s[i] == s[i + 1])
            {
                string r2 = find(s, i, i + 1);
                if (r2.size() > longest.size())
                {
                    longest = r2;
                }
            }
        }

        return longest;
    }

    string find(string s, int left, int right)
    {
        while (left >= 0 && right < s.size() && s[left] == s[right])
        {
            left--;
            right++;
        }

        return s.substr(left + 1, right - left - 1);
    }
};
