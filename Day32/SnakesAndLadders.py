# LeetCode: Snakes and Ladders
# Difficulty: Medium
# Approach: BFS + Board Flattening
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
#
# Explanation:
# - Convert the 2D board into a 1D array to simulate moves easily.
# - Use BFS to find the minimum number of dice rolls to reach the last cell.
# - Each BFS level represents one dice roll.
# - Use a visited set to avoid revisiting cells.

import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Convert 2D board to 1D array
        arr = [0] * (n * n + 1)
        idx = 1
        left_to_right = True

        for r in range(n - 1, -1, -1):
            if left_to_right:
                for c in range(n):
                    arr[idx] = board[r][c]
                    idx += 1
            else:
                for c in range(n - 1, -1, -1):
                    arr[idx] = board[r][c]
                    idx += 1
            left_to_right = not left_to_right

        # BFS
        queue = collections.deque([1])
        visited = set([1])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == n * n:
                    return steps

                for move in range(1, 7):
                    next_pos = curr + move
                    if next_pos > n * n:
                        continue

                    dest = arr[next_pos] if arr[next_pos] != -1 else next_pos

                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)

            steps += 1

        return -1
