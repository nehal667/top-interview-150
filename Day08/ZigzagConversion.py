# LeetCode: Zigzag Conversion
# Difficulty: Medium
# Approach: Simulate row-by-row writing (Down then Up)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# We create numRows strings. We move a pointer curr_row from top to bottom,
# then bottom to top (zigzag). Add each character to the current row.
# Finally, join all rows to get the result.

from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only 1 row (or rows >= length), zigzag doesn't change the string
        if numRows == 1 or numRows >= len(s):
            return s

        rows: List[str] = [""] * numRows
        curr_row = 0
        going_down = True

        for ch in s:
            rows[curr_row] += ch

            # Change direction at top or bottom
            if curr_row == numRows - 1:
                going_down = False
            elif curr_row == 0:
                going_down = True

            curr_row += 1 if going_down else -1

        return "".join(rows)
