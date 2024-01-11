# Runtime: 3415ms
# Memory: 18.76MB
# Link: https://leetcode.com/problems/3sum/

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums, reverse=False)
    answer = set()
    are_distinct_indexes = lambda i, l, h: i != l and i != h and l != h 

    for i in range(0, len(nums) - 2):
        l=i; h=len(nums)-1
        while(l < h):
            t = nums[i] + nums[l] + nums[h]
            if are_distinct_indexes(i, l, h) and t == 0:
                answer.add((nums[i], nums[l], nums[h]))
            if t <= 0: l += 1
            else: h -= 1
    return [list(x) for x in answer]

if __name__ == '__main__':
    assert (a := threeSum([0,0,0])) == [[0,0,0]], f"Output: {a = }"
    assert (a := threeSum([0,1,1])) == [], f"Output: {a = }"
    assert (a := threeSum([-1,0,1,2,-1,-4])) == [[-1,-1,2],[-1,0,1]], f"Output: {a = }"
    print("Accepted")
    