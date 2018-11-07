from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(p) > len(s):
            return []

        p_counts = Counter(p)
        counter = len(p_counts)

        ans = []
        start_idx = 0
        end_idx = 0

        while end_idx < len(s):
            end_char = s[end_idx]
            if end_char in p_counts:
                p_counts[end_char] -= 1
                if p_counts[end_char] == 0:
                    counter -= 1
            end_idx += 1

            while counter == 0:
                print(end_idx, start_idx)
                if end_idx - start_idx == len(p):
                    ans.append(start_idx)

                start_char = s[start_idx]
                if start_char in p_counts:
                    p_counts[start_char] += 1
                    if p_counts[start_char] == 1:
                        counter += 1
                start_idx += 1
        return ans

a = Solution()
print(a.findAnagrams('cbaebabacd', 'abc'))