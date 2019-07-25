%%time

import math

def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

nums = range(int(1e3))
for n in range(100):
    r = compute_roots(nums)