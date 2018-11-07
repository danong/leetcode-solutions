from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        if not words:
            return ans

        word_size = len(words[0])
        window_size = word_size * len(words)

        word_count = Counter(words)
        ref = dict(word_count)  # make a copy

        for i in range(0, word_size):
            start_idx = end_idx = i
            word_count = dict(ref)
            counter = len(word_count)

            while (end_idx + word_size - 1) < len(s):
                end_word = s[end_idx:end_idx + word_size]
                if end_word in word_count:
                    word_count[end_word] -= 1
                    if word_count[end_word] == 0:
                        counter -= 1

                end_idx += word_size

                while counter == 0:
                    if end_idx - start_idx == window_size:
                        ans.append(start_idx)

                    start_word = s[start_idx:start_idx + word_size]
                    if start_word in word_count:
                        word_count[start_word] += 1
                        if word_count[start_word] > 0:
                            counter += 1

                    start_idx += word_size
        return ans