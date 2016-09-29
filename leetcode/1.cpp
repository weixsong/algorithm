#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool comparer(pair<int, int> i, pair<int, int> j)
{
    return (i.first < j.first);
}

// solution: sort nums and record the num's indices, then search from left and right
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> nums_indices;
        for (int i = 0; i < nums.size(); i++)
        {
            nums_indices.push_back(pair<int, int>(nums[i], i));
        }

        sort(nums_indices.begin(), nums_indices.end(), comparer);

        int left = 0;
        int right = nums.size() - 1;
        vector<int> res;

        while (left < right)
        {
            int sum = nums_indices[left].first + nums_indices[right].first;
            if (sum == target)
            {
                res.push_back(nums_indices[left].second);
                res.push_back(nums_indices[right].second);

                return res;
            }

            if (sum < target) left++;
            else right--;
        }

        return res;
    }
};

int main()
{
    vector<int> nums = { 32,71,12,45,26,80,53,33 };

    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << endl;
    }

    vector<pair<int, int>> nums_indices;
    for (int i = 0; i < nums.size(); i++)
    {
        nums_indices.push_back(pair<int, int>(nums[i], i));
    }

    sort(nums_indices.begin(), nums_indices.end(), comparer);

    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << endl;
    }

    return 0;
}