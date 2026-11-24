import math


class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                curr_gcd = x if curr_gcd == 0 else self.gcd(curr_gcd, x)
                curr_lcm = self.lcm(curr_lcm, x)

                if prod == curr_lcm * curr_gcd:
                    ans = max(ans, j - i + 1)

        return ans