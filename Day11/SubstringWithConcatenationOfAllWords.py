# LeetCode: Substring with Concatenation of All Words
# Difficulty: Hard
# Approach: Brute force window + Frequency HashMaps
# Time Complexity: O((n - window_len) * k) where k = number of words
# Space Complexity: O(k)
#
# Explanation:
# - Build a frequency map of the given words (word_freq).
# - Each valid substring must have length = len(words) * word_len.
# - For every starting index i, scan chunks of size word_len inside the window.
# - Track counts in substr_freq; if a word is missing or count exceeds expected, break.
# - If we matched the full window, store i.

from typing import List, Dict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_freq: Dict[str, int] = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)

        word_len = len(words[0])
        window_len = len(words) * word_len
        res: List[int] = []

        for i in range(len(s) - window_len + 1):
            substr_freq: Dict[str, int] = {}
            j = i

            while j < i + window_len:
                cur_word = s[j: j + word_len]

                if cur_word not in word_freq:
                    break

                substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1

                if substr_freq[cur_word] > word_freq[cur_word]:
                    break

                j += word_len

            if j == i + window_len:
                res.append(i)

        return res
