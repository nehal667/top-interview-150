# LeetCode: Happy Number
# Difficulty: Easy
# Approach: Recursion + Digit Square Sum
# Time Complexity: O(log n) per step, repeats until it reaches 1 or a known non-happy digit
# Space Complexity: O(log n) due to recursion stack
#
# Explanation:
# - If n becomes 1 or 7, it is a happy number.
# - If n is a single digit (<10) and not 1 or 7, it is not happy.
# - Otherwise, compute sum of squares of digits and repeat using recursion.

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return self.isHappy(total)
