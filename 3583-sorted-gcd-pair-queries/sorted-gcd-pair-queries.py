from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # frequency
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)

        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = pairs with gcd exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2
            multiple = d * 2
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d
            exact[d] = pairs

        # prefix counts
        prefix = []
        values = []

        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans