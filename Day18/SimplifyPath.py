# LeetCode: Simplify Path
# Difficulty: Medium
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Split the path by '/' to get components.
# - Ignore empty strings and '.' (current directory).
# - '..' means go back one directory → pop from stack if possible.
# - Otherwise, push valid directory names to the stack.
# - Join stack elements with '/' to form the simplified path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for comp in components:
            if comp == "" or comp == ".":
                continue
            elif comp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(comp)

        return "/" + "/".join(stack)
