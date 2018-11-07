class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        char_map = {} # key: char, val: idx
        max_seen = 0
        start_idx = 0
        
        for end_idx, val in enumerate(s):
            if val in char_map:
                start_idx = max(start_idx, char_map[val] + 1)
            char_map[val] = end_idx
            max_seen = max(max_seen, end_idx - start_idx + 1)
        
        return max_seen

    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0

        seen = {}
        start_idx = 0
        end_idx = 0
        max_seen = 0

        while end_idx < len(s):
            cur = s[end_idx]
            if cur in seen and seen[cur] >= start_idx:
                start_idx = seen[cur] + 1
            else:
                seen[cur] = end_idx
                end_idx += 1

            if (end_idx - start_idx) > max_seen:
                max_seen = end_idx - start_idx
        return max_seen