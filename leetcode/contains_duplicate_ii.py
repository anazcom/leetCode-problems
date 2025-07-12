# Runtime:  27 ms
# Memory:   37.08 MB
# Link:     https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen_at = {}
        for end, value in enumerate(nums):
            if value not in last_seen_at:
                last_seen_at[value] = end
                continue  # not checking anything else

            if end - last_seen_at[value] <= k:
                return True

            last_seen_at[value] = end

        return False


sol = Solution()
assert sol.containsNearbyDuplicate([1, 1], 1)
assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3)
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1)
assert not sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
assert sol.containsNearbyDuplicate([99, 99], 2)
assert sol.containsNearbyDuplicate([2, 2], 3)
assert not sol.containsNearbyDuplicate([2], 1)
