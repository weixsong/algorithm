#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if ((m + n) % 2 == 1)
        {
            return findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) / 2 + 1);
        }
        else
        {
            int a = findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) / 2);
            int b = findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) / 2 + 1);
            return (a + b) / 2.0;
        }
    }

    int findk(vector<int>& nums1, int left1, int right1, vector<int>& nums2, int left2, int right2, int k)
    {
        if (right1 - left1 > right2 - left2)
        {
            return findk(nums2, left2, right2, nums1, left1, right1, k);
        }

        if (left1 > right1)
        {
            return nums2[left2 + k - 1];
        }

        if (k == 1)
        {
            return min(nums1[left1], nums2[left2]);
        }

        int pa = min(k / 2, right1 - left1 + 1);
        int pb = k - pa;

        int n1 = nums1[left1 + pa - 1];
        int n2 = nums2[left2 + pb - 1];
        if (n1 < n2)
        {
            return findk(nums1, left1 + pa, right1, nums2, left2, left2 + pb, k - pa);
        }
        else if (n1 > n2)
        {
            return findk(nums1, left1, left1 + pa, nums2, left2 + pb, right2, k - pb);
        }
        else
        {
            return n1;
        }
    }
};
