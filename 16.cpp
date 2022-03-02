class Solution
{
public:
    int threeSumClosest(vector<int> &A, int B)
    {
        if (A.size() < 3)
        {
            return 0;
        }
        sort(A.begin(), A.end());
        int closest = A[0] + A[1] + A[2];
        for (int i = 0; i < A.size() - 2; i++)
        {
            if (i > 0 && A[i] == A[i - 1])
                continue;
            int l = i + 1;
            int r = A.size() - 1;
            while (l < r)
            {
                int curSum = A[i] + A[l] + A[r];
                if (curSum == B)
                    return curSum;
                if (abs(B - curSum) < abs(B - closest))
                {
                    closest = curSum;
                }
                if (curSum > B)
                {
                    r--;
                }
                else
                {
                    l++;
                }
            }
        }
        return closest;
    }
};