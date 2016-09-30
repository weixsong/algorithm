class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int longest = 0;
        unordered_set<char> coverset;
        int p1 = 0;
        int p2 = 0;

        while (p2 < s.length())
        {
            char c = s[p2];
            if (coverset.find(c) == coverset.end())
            {
                coverset.insert(c);
                p2 += 1;
                int d = p2 - p1;
                if (d > longest)
                {
                    longest = d;
                }
            }
            else
            {
                while (coverset.find(c) != coverset.end())
                {
                    coverset.erase(s[p1]);
                    p1 += 1;
                }
            }
        }

        return longest;
    }
};
