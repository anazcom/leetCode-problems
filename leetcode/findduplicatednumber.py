# Runtime: 477 ms
# Memory: 23.61 MB
# Link: https://leetcode.com/problems/find-the-duplicate-number

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        fast_pointer = nums[0]; slow_pointer = nums[0]

        while  True:
            fast_pointer = nums[nums[fast_pointer]]
            slow_pointer = nums[slow_pointer]

            if fast_pointer == slow_pointer: break

        slow_pointer = nums[0]
        while fast_pointer != slow_pointer:
            fast_pointer = nums[fast_pointer]
            slow_pointer = nums[slow_pointer]

        return fast_pointer



sol = Solution()
assert  sol.findDuplicate([1,1]) == 1, "Wrong Answer"
assert  sol.findDuplicate([1,3,4,2,2]) == 2, "Wrong Answer"
assert  sol.findDuplicate([3,1,3,4,2]) == 3, "Wrong Answer"
assert  sol.findDuplicate([2,2,2,2,2]) == 2, "Wrong Answer"
assert  sol.findDuplicate([2,5,9,6,9,3,8,9,7,1]) == 9, "Wrong Answer"

1+2+3+4 