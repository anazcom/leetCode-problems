# Runtime: 46ms
# Memory: 14.75MB
# Link: https://leetcode.com/problems/two-sum/submissions/

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_index = [(num,index) for index,num in enumerate(nums)] 
    nums_index = sorted(nums_index, key=lambda x:x[0])
    l=0;h=len(nums)-1

    while l < h:
        t = nums_index[l][0] + nums_index[h][0]
        if t < target: l +=1
        elif t > target: h -= 1
        else: return [nums_index[l][1],nums_index[h][1]]
    return []


if __name__ == "__main__":
    assert twoSum([2,7,11,15], 9) == [0,1], "Wrong Answer"
    assert twoSum([3,3], 6) == [0,1], "Wrong Answer"