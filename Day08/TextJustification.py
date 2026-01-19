# LeetCode: Text Justification
# Difficulty: Hard
# Approach: Greedy + Space Distribution
# Time Complexity: O(total characters)
# Space Complexity: O(maxWidth) for building lines
#
# Explanation:
# 1) Greedily take as many words as fit in the current line.
# 2) If it's the last line OR the line has one word: left-justify.
# 3) Otherwise: fully justify by distributing spaces evenly.
#    Extra spaces go to the left gaps.

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            # 1) Pick words for the current line (greedy)
            line_len = len(words[i])
            j = i + 1

            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = len(line_words)

            # 2) Last line or single-word line -> left justify
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                # 3) Full justify
                letters = sum(len(w) for w in line_words)
                spaces_needed = maxWidth - letters
                gaps = num_words - 1

                space_each = spaces_needed // gaps
                extra = spaces_needed % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * space_each
                    if extra > 0:
                        line += " "
                        extra -= 1

                line += line_words[-1]
                res.append(line)

            i = j

        return res
