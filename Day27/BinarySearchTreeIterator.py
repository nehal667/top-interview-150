# LeetCode: Binary Search Tree Iterator
# Difficulty: Medium
# Approach: Stack (Inorder Traversal)
# Time Complexity:
#   - next(): O(1) average
#   - hasNext(): O(1)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - Use a stack to simulate inorder traversal.
# - Always keep the leftmost path on the stack.
# - next() returns the next smallest element.
# - hasNext() checks if elements are still available.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._pushLeftsUntilNull(root)

    def next(self) -> int:
        # Get the next smallest element
        node = self.stack.pop()
        self._pushLeftsUntilNull(node.right)
        return node.val

    def hasNext(self) -> bool:
        # Check if there are remaining elements
        return len(self.stack) > 0

    def _pushLeftsUntilNull(self, root: Optional[TreeNode]) -> None:
        # Push all left children to stack
        while root:
            self.stack.append(root)
            root = root.left
