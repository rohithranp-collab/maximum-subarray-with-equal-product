# maximum-subarray-with-equal-product

- **Platform:** LeetCode
- **Problem:** [3411. Maximum Subarray With Equal Products](https://leetcode.com/problems/maximum-subarray-with-equal-products/)
- **Difficulty:** Easy
- **Language:** Python

## Problem Summary

Given an array of positive integers `nums`, a contiguous subarray `arr` is **product equivalent** if:

$$\text{prod}(arr) = \text{lcm}(arr) \times \gcd(arr)$$

where:
- `prod(arr)` is the product of all elements in `arr`.
- `gcd(arr)` is the greatest common divisor of all elements in `arr`.
- `lcm(arr)` is the least common multiple of all elements in `arr`.

Return the length of the **longest** product-equivalent subarray in `nums`.

### Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10`

## Approach

1. Iterate over every possible starting index `i` from `0` to `n - 1`.
2. Extend the subarray to right index `j` (`i <= j < n`) while incrementally updating:
   - `prod`: running product of elements in `nums[i..j]`
   - `curr_gcd`: running GCD of elements in `nums[i..j]`
   - `curr_lcm`: running LCM of elements in `nums[i..j]`
3. Check if `prod == curr_lcm * curr_gcd`. Whenever true, update `ans = max(ans, j - i + 1)`.

> **Note:** Custom `gcd` and `lcm` helpers are used instead of relying solely on `math.lcm` (which was added in Python 3.9), ensuring compatibility across Python runtimes.

## Solution

```python
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
