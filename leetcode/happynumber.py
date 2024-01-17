# Runtime: 16ms
# Memory: 13.27MB
# Link: https://leetcode.com/problems/happy-number/

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        
        slow_sum = n; fast_sum = getSum(n)
        while slow_sum != fast_sum and fast_sum != 1:
            slow_sum = getSum(slow_sum); fast_sum = getSum(getSum(fast_sum))
        return fast_sum == 1

def getSum(n):
    sum = 0
    while n > 0: 
        sum += (n % 10) ** 2; n //= 10
    return sum

assert isHappy(10) == True, "Wrong Answer"
assert isHappy(19) == True, "Wrong Answer"
assert isHappy(2) == False, "Wrong Answer"
assert isHappy(3) == False, "Wrong Answer"