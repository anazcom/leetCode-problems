# Runtime: 33ms
# Memory: 13.38MB
# Link: https://leetcode.com/problems/buy-two-chocolates/

def buyChoco(prices, money):
    """
    :type prices: List[int]
    :type money: int
    :rtype: int
    """
    min_1 = min_2 = 200

    for price in prices:
        if price < min_1: 
            min_2 = min(min_1, min_2)   
            min_1 = price
        elif price < min_2:
            min_2 = price
        else: continue
    
    print(f"{min_1 = } {min_2 = }")
    left_over = money - (min_1 + min_2)
    return money if left_over < 0 else left_over


assert buyChoco([69,91,78,19,40,13], 94) == 62, "Wrong Answer"

    